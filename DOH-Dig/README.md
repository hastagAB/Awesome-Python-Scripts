# doh-dig

A python dig script that returns json dns record lookup using cloud flares DNS servers. 

## Usage 
```
Usage:
  doh-dig type <type> <record> 
  doh-dig ptr <ip>
  doh-dig (-h | --help)
  doh-dig --version

```

### requirements
* [docopt]: https://github.com/docopt/docopt
* [requests]: https://pypi.org/project/requests/

### Examples

#### lookup and A record for google.com
./doh-dig type a google.com  |python -m json.tool 
 ```
 [
    {
        "name": "google.com.",
        "type": 1,
        "TTL": 235,
        "data": "172.217.19.174"
    }
]
```

#### lookup reverse record for an IP
 ./doh-dig ptr 1.1.1.1 |python -m json.tool
 ```
 [
    {
        "name": "1.1.1.1.in-addr.arpa.",
        "type": 12,
        "TTL": 1345,
        "data": "one.one.one.one."
    }
]
```