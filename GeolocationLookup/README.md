# Geolocation Lookup

This script make use of [IP2Location.io API](https://www.ip2location.io/) to query enrich geolocation information for an IP address. The script supports both normal API call and keyless API call. The keyless API had a limitation of 500 queries per day. Once this limit is reached, any additional API calls will fail until the time period resets at 00:00 UTC daily.

## Parameters

|Parameter| Description |
|--|--|
|-k, --apikey  | IP2Location.io API Key. You can sign up a free one from https://www.ip2location.io/sign-up. If not provided, the script will use keyless API. |
|-p, --ip | IP address to be query for. If not provided, the source IP address will be use to query. |


## Usage

Before running the script, make sure install the required libraries first:

```
    pip install -r requirements.txt
```

To perform normal query with the API Key, you can use `python GeolocationLookup.py -k <your_IP2Locatio.io_API_Key> -p <ip_address>`. Replaced the relevant values before run the command.

For keyless API call, you can run`python GeolocationLookup.py` or `python GeolocationLookup.py -p <ip_address>`.

For a successful call, you shall getting a JSON result printed out. For instance, you will see the following output for the IP address 8.8.8.8 for keyless API:

```json
{
    "ip": "8.8.8.8",
    "country_code": "US",
    "country_name": "United States of America",
    "region_name": "California",
    "city_name": "Mountain View",
    "latitude": 37.38605,
    "longitude": -122.08385,
    "zip_code": "94035",
    "time_zone": "-07:00",
    "asn": "15169",
    "as": "Google LLC",
    "is_proxy": false,
    "message": "Limit to 500 queries per day. Sign up for a Free plan at https://www.ip2location.io to get 30K queries per month."
}
```
