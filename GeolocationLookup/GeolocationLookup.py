import sys
import json
import argparse
import requests

# Define functions

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--apikey', metavar='IP2Location.io API Key.')
    parser.add_argument('-p', '--ip', metavar='Specify an IP address.')

    return parser

# Define variables
keyless = False
self_ip_query = False
parameters = {}

if len(sys.argv) > 1:
    # check if API key is provided or not
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    if args.apikey is None:
        keyless = True
    else:
        parameters['key'] = args.apikey
    if args.ip is None:
        self_ip_query = True
    else:
        parameters['ip'] = args.ip
else:
    # Assuming using Keyless API
    keyless = True

if keyless:
    print(f"Calling keyless API now...")
    if len(parameters) > 0:
        r = requests.get('https://api.ip2location.io/', params=parameters) 
    else:
        r = requests.get('https://api.ip2location.io/')
else:
    print(f"Calling API now...")
    if len(parameters) > 0:
        r = requests.get('https://api.ip2location.io/', params=parameters) 
    else:
        r = requests.get('https://api.ip2location.io/')

if r.json() == None:
    print(f"Unexpected error, please try again later.")
elif 'error' in r.json():
    print(f"IP2Location.io API error: {r.json()['error']['error_message']}")
else:
    print(r.json())
