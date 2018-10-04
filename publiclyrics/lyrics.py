import requests
import json


x="https://api.lyrics.ovh/v1/adele/hello"
r=requests.get(x)

json_data=r.json()
print(json_data['lyrics'])
