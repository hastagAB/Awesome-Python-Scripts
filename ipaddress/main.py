# Import Part
from os import system
try:
    from requests import get, Response, ReadTimeout
except ImportError:
    system('pip install -r requirements.txt')
    exit('Please run the program again')

# Api
ip_provider = r"https://api.techniknews.net/ipgeo/"

print('Getting ip info. It\'s may take some time ...')

try :
    response: Response = get(ip_provider, timeout=20)
    if response.status_code != 200:
        exit(f"[{response.status_code} Error]")
    
    # Getting info from json file   
    JsonResponse: dict = response.json()
    if JsonResponse['status'] == 'success':
        ip: str = JsonResponse["ip"]
        city: str = JsonResponse["city"]
        area: str = JsonResponse["regionName"]
        zip_code: str = JsonResponse["zip"]
        country: str = JsonResponse["country"]
        continent: str = JsonResponse['continent']
        isp: str = JsonResponse['isp']
        IsMobile: bool = JsonResponse['mobile']
        UseProxy: bool = JsonResponse['proxy']
    else:
        exit('The operation was unsuccessful. Try again')

    print(
        f"""
        IP address   : {ip}
        Continent    : {continent}
        Country      : {country}
        City         : {city}
        Area         : {area}
        Postal code  : {zip_code}
        Isp          : {isp}
        Using Mobile : {IsMobile}
        Using Proxy  : {UseProxy}
        """
    )
except ConnectionError:
    exit("Error !! Check your internet connection")
except KeyboardInterrupt:
    exit('The operation canceled by user')
except ReadTimeout:
    exit('Timeout has reached')