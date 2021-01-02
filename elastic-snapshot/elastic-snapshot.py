#!/usr/bin/python3
''' elastic-snapshot.py elasticsearch snapshot utility
default action is to get a list of snapshots for localhost on port 9200 and the backups location
optional args: 
    (-a list |--action=list) snapshot action to perform
    (-H localhost:9200 |--hostname=localhost:9200) 
    (-i testing |--index=testing) index name to work on                
    (-l backups |--location=backups) location
    (-n |--noop) execute script as noop, print web calls and exit.
    (-p 2020.01 |--period=2020.01) period of snapshot to take, will have * appended to select additional indices
    (-r|--reason=daily) snapshot reason 
    (-v|--verbose) increase standard output verbosity
'''
import json, os, requests, time
import datetime as dt
from getpass import getuser



def get_snapshot_listing(options):
    url = "http://{host}/_cat/snapshots/{sp}?v".format(
        sp=options.snapshot_pool, host=options.host_name
    )
    if options.noop:
        return url
    else:
        #do the real stuff
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            return "Error in making request.  received {}: {}".format(r.status_code, r.text)


def create_snapshot(options):
    ''' creates a snapshot with the specified options using this format of web API request
    curl -X PUT "localhost:9200/_snapshot/my_repository/snapshot_2?wait_for_completion=true&pretty" -H 'Content-Type: application/json' -d'
    { "indices": "index_1,index_2",
      "ignore_unavailable": true,
      "include_global_state": false,
      "metadata": {
        "taken_by": "user123",
        "taken_because": "backup before upgrading" } } '''

    indexname = options.index_name
    period = options.period
    timestamp = dt.datetime.today().strftime('%Y%m%d_%H%M')
    # use special testing period for indices to snapshot if defined
    if 'testing' in options and options.testing:
        indices = indexname
        snapshot_name = "{i}-{p}-{d}".format(i="-".join(indexname.split(',')[0].split('*')), p=period,
                            d=timestamp)
    else:
        snapshot_name = "{i}-{p}-{d}".format(i=indexname.strip('*'), p=period, 
                        d=timestamp)
        indices = "{i}-{p}*".format(i = indexname, p=period)        

    url = "http://{host}/_snapshot/{sp}/{sn}".format(
        sp=options.snapshot_pool, host=options.host_name, sn=snapshot_name
    )
    payload = { "indices": indices,
        "ignore_unavailable": "true",
        "include_global_state": "false",
        "metadata": {
            "taken_by": getuser(),
            "taken_because": "Snapshot updated {d} for: {r}".format(d=timestamp,
            r=options.reason)
        } }
    print("create snapshot {} with payload: {}".format(snapshot_name, payload))
    if options.noop:
        print("Would have called url: {url}\n with payload: {pl}".format(url=url, pl=payload))
        return 200
    else:
        sleep_count = 0
        while check_snapshot_inprogress(options):
            sleep_count += 1
            if options.verbose:
                print("A snapshot is running currently, script has slept {} times so far".format(
                    sleep_count
                ))
            time.sleep(300)
            if sleep_count > 20:
                print("Snapshot still running, exceeded 10 sleep cycles")
                exit(2)
        snap_result = requests.put(url, json=payload)
        if snap_result.status_code == 200 and options.verbose:
            print("Requested: {}".format(snap_result.json()))
        else:
            print("Error encountered {code}: {response}".format(code=snap_result.status_code,
                                                    response=snap_result.json()))
        return snap_result.status_code


def restore_snapshot(options):
    print("TODO: restore snapshot with options: {}".format(options))


def check_snapshot_inprogress(options):
    snapshot_list = get_snapshot_listing(options)
    for line in [line for line in snapshot_list.split('\n')]:
        if 'IN_PROGRESS' in line.split():
            if options.verbose:
                print("snapshot in progress: {}".format(line))
            return 'IN_PROGRESS' in snapshot_list


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='''Command line utility to take snapshots of elasticsearch indices.
    Snapshot is created or updated.''')
    parser.add_argument('--action', '-a', action='store', dest='action', default='list',
            help="what snapshot action to perform: list, create")
    parser.add_argument('--host', '-H', action='store', dest='host_name', default='localhost:9200', 
            help="elasticsearch host")
    parser.add_argument('--index', '-i', action='store', dest='index_name', default='test*',
            help="Name of index to snapshot")
    parser.add_argument('--location', '-l', action='store', dest='snapshot_pool', default='backups', 
            help="Name of snapshot location")
    parser.add_argument('--noop', '-n', action='store_true', default=False, help="just print expceted call")
    parser.add_argument('--period', '-p', action='store', dest='period', default='2020.01', 
            help="period of snapshots to take")
    parser.add_argument('--reason', '-r', action='store', dest='reason', 
            default='not specified', help="text description about why snapshot was taken")
    parser.add_argument('--testing','-t', action='store_true', default=False,
            help="allows multiple indices to be listed for --index instead of default <index_name>-<period> for testing")
    parser.add_argument('--verbose', '-v', action='store_true', default=False, help="Show verbose output for script")
    options = parser.parse_args()

    action = options.action

    if action == 'list':
        print(get_snapshot_listing(options))
    elif action == 'create':
        create_snapshot(options)
    else:
        print("{action} is not a valid option.\nTry -h|--help for assistance".format(action=action))
