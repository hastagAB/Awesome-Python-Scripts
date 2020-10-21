### elastic-snapshot.py
This python3 script helps create snapshots in an elasticsearch cluster.  Setting up elasticsearch and creating a snapshot repository are covered in the [elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-restore.html)  If a snapshot is already in progress it will sleep for 5 minutes and try again.
- requires the requests library to be installed
- The default behavior is to get a list of snapshots for localhost and the backups snapshot repository
- snapshots are created with at least a minimum of meta data: {taken_by: username, taken_because: 'Snapshot updated <timestamp> for: not specified}
- This script assumes indices are named with dates in the form indexname-YYYY.MM.DD so it can use the period to select indices
- `--testing` flag allows a comma separated list of indices to be supplied.  In this case, the period will be used only for the snapshot name.
- optional args and default values:
```
$   python3 elastic-snapshot.py [optional args]
    (-a|--action=list) snapshot action to perform (list, create, restore)
    (-h|--hostname=localhost:9200) 
    (-i test* |--index=test*) index name pattern to work on                
    (-l backups|--location=backups) snapshot repository name
    (-n|--noop) do not actually perform the API call but print it to stdout
    (-p|--period=2020.01) period for snapshot, unless --testing every index matching pattern indexname*-<period>* is implied
    (-r|--reason='not specified') snapshot reason for inclusion in metadata
    (-t|--testing=False) allows specifying multiple index names in --index
    (-v|--verbose=False) get verbose output to std out
```
- examples:
```
$ python3 elastic-snapshot.py
# returns a list of the snapshots from localhost:9200

$ python3 elastic-snapshot.py --action create --index filebeat* --period 2020.08
# creates a snapshot named filebeat-2020.08-<timestamp> that includes all indices that match the pattern filebeat*-2020.08*

$ python3 elastic-snapshot.py -a create -i metricbeat* -p 2020.08 -l my_snapshots -v
# creates a snapshot named metricbeat-2020.08-<timestamp> in the snapshot repository named my_snapshots.  This snapshot will contain any index that matches the pattern metricbeat*-2020.08.  Verbose output will be printed to standard output
```