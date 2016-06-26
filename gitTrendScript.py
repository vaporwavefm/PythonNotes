# George Juarez


from bs4 import BeautifulSoup
import requests

# I guess this belonged as the second parameter in BeautifulSoup(a,b)
# from_encoding=encoding

resp = requests.get("https://github.com/trending")
encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
soup = BeautifulSoup(resp.content, "html.parser")
for link in soup.find_all('a', href=True):
    print(link['href'])


