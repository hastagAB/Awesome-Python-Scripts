import requests

ip_provider = "http://ipaddr.in/json"
user_agent = {
    'User-agent': 'curl/7.82.0'
    }
try :
    web_request = requests.get(ip_provider, headers=user_agent , timeout=10)
    response = web_request.json()

    ip = response["ip"]
    city = response["city"]
    area = response["region_name"]
    zip_code = response["zip_code"]
    country = response["country"]

    print(
        f"""
        IP address  : {ip}
        City        : {city}
        Area        : {area}
        Postal code : {zip_code}
        Country     : {country}
        """
    )
except :
    print("Error !! Check your internt connection")