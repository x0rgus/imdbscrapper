import requests
from bs4 import BeautifulSoup
import random

user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
URL = "https://www.imdb.com/chart/moviemeter/"
page = requests.get(URL, headers=HEADERS)

OPERATION_STATUS = False
page = requests.get(URL, headers=HEADERS)

match page.status_code:
    case 200:
        OPERATION_STATUS = True
    case 403:
        page = requests.get(URL, headers={'User-Agent': random.choice(user_agents_list)})
        if page.status_code == 200:
            OPERATION_STATUS = True
        else:
            print("failed to get page")
    case _:
        print("Failed to get page")


if OPERATION_STATUS == True:
    soup = BeautifulSoup(page.content, "html.parser")
    page_content = soup.find('tbody', class_='lister-list').findAll('tr')
    names = []
    years = []
    rating = []
    all_movies = []

    for movie in page_content:
        placeholder_movie = {
            "Name":"",
            "Year":"",
            "Rating":"",
        }
        try:
            name = movie.find('td', class_='titleColumn').a.text
            placeholder_movie["Name"] = name
        except AttributeError:
            placeholder_movie["Name"] = ("No name avaliable")
        
        try:
            year = movie.find('td', class_='titleColumn').span.text
            placeholder_movie['Year'] = year
        except AttributeError:
            placeholder_movie["Year"] = ("No release date")
        
        try:
            rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
            placeholder_movie["Rating"] = (rating)
        except AttributeError:
            placeholder_movie["Rating"] = ("-")
        
        all_movies.append(placeholder_movie)
print(all_movies)