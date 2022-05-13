#!/usr/bin/python3
# http://sch37.minsk.edu.by
# div.sch_article

from bs4 import BeautifulSoup
import requests as req
resp = req.get("http://sch37.minsk.edu.by")
soup = BeautifulSoup(resp.text,'lxml')

# with open("http://sch37.minsk.edu.by","r") as f:
# 	contents= f.read()
# 	soup = BeautifulSoup(contents,'lxml')
app = soup.body

# app_childs = [e.name for e in app.descendants if e.name is not None]
# print(app_childs)

for tag in app.find_all("a"):
	print("{0}: {1}".format(tag.name, tag.text))
