from bs4 import BeautifulSoup
import pymongo
import urllib2
from time import sleep

CORE_LINK = "https://allpoetry.com/"

connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['poems']
collection = db['poem_collection']

for i in xrange(6,15):
	
	try:
	
		site = urllib2.urlopen(CORE_LINK + "classics/famous_poems?page=%d" % i).read()
		soup =  BeautifulSoup(site, 'html.parser')

		poem_urls = tuple(x.a['href'] for x in soup.findAll("div", {"class": "heading"}))

		for url in poem_urls:

			try:
				s = urllib2.urlopen(CORE_LINK + url).read()
				soup = BeautifulSoup(s, 'html.parser')

				print url

				try:
					title = soup.findAll("h1", {"class": "title"})[0].getText()[:-10]
				except IndexError,e:
					continue

				if not collection.find_one({"title":title}):
					
					t_div = soup.findAll("div", {"class": "poem_body"})
					if len(t_div) > 0:
						t_div = t_div[0]
						if t_div.p:
							t = t_div.p.getText()
						else:
							t = t_div.getText()
								
						collection.insert_one({"poem": t, "title":title})

			except urllib2.URLError,e:
				continue

			sleep(5)
	except urllib2.HTTPError,e:
		break
	except urllib2.URLError, e:
		continue

	sleep(2)

	