import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxy():
    url = "https://www.sslproxies.org/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), 
                                                                      map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

def proxy_request(request_type, url, **kwargs):
    while 1:
        try:
            proxy = get_proxy()
            print(f"Using proxy {proxy['https']}")
            response = requests.request(request_type, url, proxies=proxy, timeout=5, **kwargs)
            break
        except Exception as e:
            print(e)
    return response


if __name__ == "__main__":
	r = proxy_request('get', "https://www.youtube.com/IndianPythonista")