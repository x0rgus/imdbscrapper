import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/moviemeter/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

infomovies = soup.find('tbody', class_='lister-list').findAll('tr')
names = []
years = []
ratings = []
posters = []
links = []
for movie in infomovies:
    try:
        nome = [movie.find('td', class_='titleColumn').a.text]
        names.extend(nome)
    except AttributeError:
        names.extend("No name info")

    try:
        ano = [movie.find('td', class_='titleColumn').span.text]
        years.extend(ano)
    except AttributeError:
        years.extend("No year info")
    try:
        rating = [movie.find('td', class_='ratingColumn imdbRating').strong.text]
        ratings.extend(rating)
    except AttributeError:
        ratings.extend("-")
    poster = movie.find('td', class_='posterColumn').img
    posters.extend(poster)

    link = movie.find('td', class_='titleColumn').a
    links.extend(link)

# print(names)
# print(years)
# print(ratings)
print(posters)
print(links)