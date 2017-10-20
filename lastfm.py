# George Juarez
# Last.fm recorder

from selenium import webdriver
from bs4 import BeautifulSoup
import sys

urls = ["https://www.last.fm/user/TreeckoEater/library/artists?date_preset=ALL",
	"https://www.last.fm/user/TreeckoEater"]

def readURL(url,tag,tag_class):
	browser = webdriver.Chrome("C:\chromedriver.exe")
	browser.get(url) 
	soup = BeautifulSoup(browser.page_source, "html.parser")
	res_list = soup.find_all(tag,tag_class)
	browser.quit()
	return res_list

def processURL(urls):
	artists = readURL(urls[0],"a","link-block-target")
	counts = readURL(urls[0], "span","countbar-bar-value-wrapper")
	t = readURL(urls[1],"p","header-metadata-display")

	for i in range(0,len(artists)):
		if("Join Last.fm" in artists[i].contents[0].encode("utf-8")):
			del artists[i]

	for count in counts:
		count.contents[0] = count.contents[0].encode("utf-8").replace("\n", "")
		count.contents[0] = count.contents[0].replace(",", "")
		count.contents[0] = count.contents[0].replace(" ", "")

	total = t[0].contents[0].encode("utf-8").replace('<a href="/user/TreeckoEater/library">',"")
	total = total.replace("</a>","")
	total = total.replace(",","")
	print total

	percents = range(50)
	for i in range(0, len(percents)):
		percents[i] = 100 * (float(counts[i].contents[0]) / float(total))

	for i in range(0,len(artists)):
		print artists[i].contents[0].encode("utf-8"), ":\t", counts[i].contents[0], " (", percents[i], "%) "



if __name__ == '__main__':
	processURL(urls)