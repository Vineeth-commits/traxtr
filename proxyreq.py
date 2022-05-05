import requests
from bs4 import BeautifulSoup as bs
from random import choice
def get_proxies():
    proxy_url = "https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt"
    r = requests.get(proxy_url)
    soup = bs(r.content, "html.parser").find_all("td",{"class":"blob-code blob-code-inner js-file-line"})
    proxies = [proxy.text for proxy in soup]
    return proxies

def get_random_proxy(proxies):
    return {"https" : choice(proxies)}

proxies = get_proxies()

def get_working_proxies():
    working = []
    for i in range(30):
        proxy = get_random_proxy(proxies)
        print(f"using {proxy}...")
        try:
            r = requests.get("https://www.google.com",proxies=proxy, timeout=3)
            print(r.status_code)
            if r.status_code == 200:
                working.append(proxy)
        except:
            pass
    return working
