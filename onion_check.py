import requests
import socks
import socket
import sys
from bs4 import BeautifulSoup

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
socket.socket = socks.socksocket

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# To check the IP just remove the comment from next line....
print("Tor Connection Check")
try:
    tor_ip = requests.get('https://ident.me').text
    print('Tor_IP: ', tor_ip)
    print("Tor Connection Success ")
except Exception as e:
    print("Error: Configure Tor as service")
    print("For quick setup refer: https://miloserdov.org/?p=1839")
    exit()
# Submit a text file containing an onion URL in a line
in_file = input("Submit the URL File: ")
input_file = open(in_file, 'r')

for url in input_file:
    url = url.rstrip('\n')
    try:
        data = requests.get(url, proxies=proxies)
    except:
        data = 'error'
    if '200' in str(data):
        status = 'Active'
        soup = BeautifulSoup(data.text, 'html.parser')
        for url_title in soup.find_all('title'):
            url_title = str(url_title)
            url_title = url_title.replace('<title>', '')
            url_title = url_title.replace('</title>', '')
    else:
        status = "Inactive"
        url_title = 'NA'
    print(url, ': ', status, ': ', url_title)
