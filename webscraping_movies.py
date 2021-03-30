import requests
from bs4 import BeautifulSoup

base_url = "https://letterboxd.com/"  # base url of letterboxd that will be used to obtain results later
 
# TODO
url = "https://letterboxd.com/films/ajax/popular/year/2021/size/small/" 
helper_url = "https://letterboxd.com/films/ajax/"


result_list = []  # list of the obtained titles resulted from the search
while True:

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html5lib')
    
    for row in soup.findAll('li', attrs = {"class": "listitem poster-container"}):
        
        movie = {}
        
        # title and url
        movie['title'] = row.div.a['title']
        movie_url = f"{base_url}{row.div.a['href']}" # TODO
        movie['url'] = movie_url
        
        # poster
        try:
              movie['img'] = row.div.img['srcset']
        except:
              movie['img'] = None

        # get more info about movie using its url
        mres = requests.get(movie_url)
        msoup = BeautifulSoup(mres.content, 'html5lib')
        
        # synopsis
        try:
            movie['synopsis'] = msoup.find("meta",  property="og:description")["content"]
        except:
            movie['synopsis'] = None
        
        # director    
        movie['director'] = msoup.find("meta", {"name": "twitter:data1"}).attrs['content']
        
        result_list.append(movie)

        break
        
    next_url = soup.find('a', attrs = {"class": "next"})
    next_url = next_url['href'] if next_url else None   
    
    if next_url:
        next_url = next_url[7:-1]
        url = f"{helper_url}{next_url}"
    
        print(url)
    else:
        break

print(result_list)

# TODO
# save results to csv
