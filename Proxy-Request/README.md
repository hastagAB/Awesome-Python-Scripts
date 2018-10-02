# Web proxy request application using Python


A quick, reliable and random Web Proxy request application using Python.

## 3rd party libraries used

- requests

- bs4

## Usage

```
from proxy_request import proxy_request

r = proxy_request('get', "https://httpbin.org/ip")

print(r.json())
```