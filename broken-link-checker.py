import requests
from bs4 import BeautifulSoup
import time
import sys
import validators

print('''\033[33m
  _                      
 |_) ._ _  |   _  ._ __ |  o ._  | __ /  |_   _   _ |   _  ._ 
 |_) | (_) |< (/_ | |   |_ | | | |<   \_ | | (/_ (_ |< (/_ |                                         
                                            beta v0.0.1 && \033[35m@zerbaly3v\033[0m                                                                                                                                                                                              
''')

headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
url = sys.argv[1]

def get_urls(url):
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('a')
  
    for link in links:
        if link.get('href') is not None and link.get('href').startswith('http'):
            is_url = link.get('href')
            res_link = requests.get(is_url)
            time.sleep(1)
            print(f"{is_url} - [\033[31;42m{res_link.status_code}\033[0m]")
        else:
            pass
        
if  validators.url(url):
    try:
        get_urls(url)
    except KeyboardInterrupt :
        input("Exit to enter")  
    except Exception as err :
        print(" ERORR: ",err)
        input("Exit to enter")
else:
    input("invalid url! Exit to enter\n")
