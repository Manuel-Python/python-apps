from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")


for movie in movies:
    #print(story.getText())
    print(movie.getText())