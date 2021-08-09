import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# To check the IP just remove the comment from next line....
print("Tor Connection Check")
try:
    system_ip = requests.get('https://ident.me', proxies=proxies).text
    tor_ip_list = requests.get('https://check.torproject.org/exit-addresses').text
    if system_ip in tor_ip_list:
        print('Tor_IP: ', system_ip)
        print("Tor Connection Success ")
except:
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
    if data != 'error':
        status = 'Active'
        status_code = data.status_code
        soup = BeautifulSoup(data.text, 'html.parser')
        page_title = str(soup.title)
        page_title = page_title.replace('<title>', '')
        page_title = page_title.replace('</title>', '')
    elif data == 'error':
        status = "Inactive"
        status_code = 'NA'
        page_title = 'NA'
    print(url, ': ', status, ': ', status_code, ': ', page_title)
