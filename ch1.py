# remember to install lxml as a pharser.

from bs4 import BeautifulSoup
import requests

html_str="http://www.google.com"
r = requests.get(html_str)
r.encoding="utf8"
soup=BeautifulSoup(r.text,"lxml")

tag = soup.div
print(tag.get_text("-"))