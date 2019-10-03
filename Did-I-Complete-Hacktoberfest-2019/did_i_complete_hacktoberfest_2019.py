#!/usr/bin/env python3

from urllib import request
import json
from datetime import datetime
from dateutil.tz import tzutc
from dateutil.parser import parse
import sys

start_time = datetime(2019, 10, 1, 0, 0, tzinfo=tzutc())

def check_done(username):
    """Checks if user has made pull quota"""
    
    count = 0
    resp = request.urlopen(f"https://api.github.com/users/{username}/events")

    for event in json.loads(resp.read()):
        if event['type'] == "PullRequestEvent" and event['payload']['action'] == "opened":
            time = parse(event['created_at'])
            if time >= start_time:
                count += 1

    return f"Yes: {username} is done with {count} pull requests" if count >= 4 else f"No: {username} needs {4 - count} more pull requests"


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(check_done(sys.argv[1]))
    else:
        print("Usage: did_i_complete_hacktoberfest_2019.py <github username>")
