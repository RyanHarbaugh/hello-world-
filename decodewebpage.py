#practise pythong exercise17
#Use the BeautifulSoup and requests Python packages 
# to print out a list of all the article titles on the 
# New York Times homepage.

import requests
from bs4 import BeautifulSoup

#use request library to load HTML of page into Python
url = 'http://www.nytimes.com'
r = requests.get(url)
#set up beautifulsoup to process the html
soup = BeautifulSoup(r.text, features="lxml")


for story_heading in soup.find_all(class_="e1voiwgp0"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0])
        















