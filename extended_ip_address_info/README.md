# Extended IP address info

View extended info about your public IP address from the terminal.

The python script runs `curl` with the following parameters
```bash
curl -H "Accept: application/json" https://ipinfo.io/json
```

## Create virtual environment and run
Create virtual environment.
```bash
python3 -m venv /path/to/new/virtual/environment
```

Activate virtual environment.
```bash
cd <file folder>
source bin/activate
```

Install required libraries.
```bash
pip install -r requirements.txt
```

**Run program.**
```bash
python extended_ip_address_info.py
```

Deactivate virtual environment.
```bash
deactivate
```

## Output
Output should be in the form of the following:
```json
{
  "ip": "xxx.xxx.xxx.xxx",
  "city": "A_city",
  "hostname": "host.isp-website.com",
  "region": "A_region",
  "country": "Country code",
  "loc": "coordinates",
  "org": "AS-number ISP-name",
  "postal": "postal-code",
  "timezone": "Europe/City",
  "readme": "https://ipinfo.io/missingauth"
}
```