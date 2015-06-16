import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen("http://www.slashdot.org")
soup = BeautifulSoup(page)

link = soup.find('link', type='application/rss+xml')
print link['href']