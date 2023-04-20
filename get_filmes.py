import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/moviemeter/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

infofilmes = soup.find('tbody', class_='lister-list').findAll('tr')




for filme in infofilmes:
        try:
            nome = [filme.find('td', class_='titleColumn').a.text]
            print(nome)
        except AttributeError:
            print("sem nome")

        try:
            ano = [filme.find('td', class_='titleColumn').span.text]
            print(ano)
        except AttributeError:
            print("sem ano")
        try:
            rating = [filme.find('td', class_='ratingColumn imdbRating').strong.text]
            print(rating)
        except AttributeError:
            print("-")

        poster = (filme.find('td', class_='posterColumn').img)
        print('poster:', poster["src"])

        link = (filme.find('td', class_='titleColumn').a)
        print('link:', link["href"])
        print('''
        ''')


