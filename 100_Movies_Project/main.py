import requests
from bs4 import BeautifulSoup
import html

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

films_list = [title.getText() for title in soup.select(selector="h3.title")]

films_list = films_list[::-1]

with open("movies.txt", mode="w") as file:
    for film in films_list:
        file.write(html.unescape(str.replace(film, r'â', '-')) + "\n")


