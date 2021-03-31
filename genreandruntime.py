import requests
from bs4 import BeautifulSoup
   
URL = "https://letterboxd.com/film/the-ascent/"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')

# try to extract genres and runtime to use in filters.

# genres
m1 = soup.find('div', attrs = {'class':"text-sluglist capitalize"})
m1 = m1.findAll('a', attrs = {'class':"text-slug"})

genres = []
for i in m1:
    genres.append(i.text)
    
print(genres)

# runtime
m1 = soup.find('p', attrs = {'class':"text-link text-footer"})

print(int(m1.text.lstrip().split("mins",1)[0]))
