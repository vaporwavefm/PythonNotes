# George Juarez

import requests
from bs4 import BeautifulSoup

def getURL(page):
    """
    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def main():
    url = "https://github.com/trending"
    response = requests.get(url)

    # parse html
    page = str(BeautifulSoup(response.content, "html.parser"))
    print("The top trending projects on Github are: ")
    
    while True:
        url, n = getURL(page)
        page = page[n:]
        parseCon = "/contributors"
        parseHTTP = "http://"
        parseHTTPS = "https://"
        parseSEARCH = "/search"
        if url:
            if url.find(parseCon) == -1 and url.find(parseHTTPS) == -1 and url.find(parseHTTP) == -1 and url.find(parseSEARCH) == -1 :
                print("https:/github.com",url, sep = "")
        else:
             break


# call main
main()
