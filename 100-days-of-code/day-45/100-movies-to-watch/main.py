from requests import get
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movie_titles = reversed([movie.getText() for movie in soup.find_all(name="h3", class_="title")])
# a_list = {1, 2, 3, 4}
# a_list_reversed = a_list[::-1]
with open(file="./best_films.txt", mode="w", encoding='utf-8') as file:
    for title in movie_titles:
        file.write(f"{title}\n")
