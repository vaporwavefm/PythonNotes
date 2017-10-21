# George Juarez
# Last.fm recorder

from selenium import webdriver # HIIII MAKE SURE YOU PUT YOUR CHROME DRIVER IN YOUR C:/ LOCATION THXBBGURL
from bs4 import BeautifulSoup
import sys

# urls = ["https://www.last.fm/user/TreeckoEater/library/artists?date_preset=ALL", "https://www.last.fm/user/TreeckoEater"]

def buildCustomURL(username):
	url_list = []
	url_list.append("https://www.last.fm/user/" + username + "/library/artists?date_preset=ALL")
	url_list.append("https://www.last.fm/user/" + username)
	return url_list

def readURL(url,tag,tag_class): # I know selenium and BS is slow af...but...ghost.py hates me lol
	browser = webdriver.Chrome("C:\chromedriver.exe")
	browser.get(url) 
	soup = BeautifulSoup(browser.page_source, "html.parser")
	res_list = soup.find_all(tag,tag_class)
	browser.quit()
	return res_list # returns list of all elements inside specified tag and class

def encodeList(res_list):
	for value in res_list:
		value.contents[0] = value.contents[0].encode("utf-8") # encode that shnizz
	return res_list # ain't no [u'Value'] in my christian household

def processURL(username):
	urls = buildCustomURL(username)
	artists = encodeList(readURL(urls[0],"a","link-block-target")) # snags top 50 artists from user library
	counts = encodeList(readURL(urls[0], "span","countbar-bar-value-wrapper")) # snags top 50 scrobble counts from user library
	t = encodeList(readURL(urls[1],"p","header-metadata-display")) # t is total number of scrobbles that the user has, unformatted

	for i in range(0, len(artists) - 1): 
		if("Join Last.fm" in artists[i].contents[0]): # I can't believe last.fm gotta do me like that
			del artists[i]

	for count in counts: # ALL THE REPLACES LOL
		count.contents[0] = count.contents[0].replace("\n", "").replace(",", "").replace(" ", "")

	total = t[0].contents[0].replace('<a href="/user/TreeckoEater/library">',"")
	total = total.replace("</a>","")
	total = total.replace(",","")

	percents = range(50)
	for i in range(0, len(percents)):
		percents[i] = 100 * (float(counts[i].contents[0]) / float(total))

	for i in range(0,len(artists)):
		print ''.join(map(str,[artists[i].contents[0], ":\t", counts[i].contents[0], " (", percents[i], "%) "]))
		# print artists[i].contents[0], ":\t", counts[i].contents[0], " (", percents[i], "%) "

if __name__ == '__main__':
	processURL(sys.argv[1])
