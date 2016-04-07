"""Import Packages"""

import requests
from bs4 import BeautifulSoup

""""Establish Connection"""

r=requests.get("http://www.imdb.com/search/title?title_type=feature&num_votes=20000,&sort=user_rating&year=2000,2016")
soup = BeautifulSoup(r.content)


for movie in soup.find_all("td","title"):
    title = movie.find("a").contents[0]
    year = movie.find("span", "year_type").contents[0]
    genre = movie.find ("span", "genre").findAll("a")
    genre = [g.contents[0] for g in genre]
    runtime = movie.find("span", "runtime").contents[0]
    rating = movie.find("span", "value").contents[0]
    outline = movie.find("span", "outline").contents[0]
    print title, genre, runtime, rating, outline, year
    
                                    
