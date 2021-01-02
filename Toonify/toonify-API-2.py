import argparse
import requests

aq = argparse.ArgumentParser()
aq.add_argument('-i', '--input', required=True, help="input image link")

aq.add_argument('-k', '--apikey', required=True, help="api-key")

args = vars(aq.parse_args())

r = requests.post(
    "https://api.deepai.org/api/toonify",
    files={
        'image': args['input'],
    },
    headers={'api-key': args['apikey']}
)
print(r.json()['output_url'])
