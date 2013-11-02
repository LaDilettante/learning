from bs4 import BeautifulSoup
import urllib2

url = "http://www.football-lineups.com/footballer/104/?t=222"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

print soup.find_all('622')
