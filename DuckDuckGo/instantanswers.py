import requests
import json
x="http://api.duckduckgo.com/?q=chandigarh&format=json&pretty=1"
r=requests.get(x)
json_data=r.json()
print(json_data['Abstract'])
print(json_data)
