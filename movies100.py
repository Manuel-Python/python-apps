from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movies = movies[::-1]

    #print(story.getText())

movieDB = {}
num = 0
count = 1
name1 = ""
for movie in movies:

    line = movie.getText()
    #name = line.split(" ")
    if ") " in line:
        name = line.split(" ")
        isFirst = True
        for n in name:
            if isFirst:
                isFirst = False

            else:
                name1 += n
                name1 += " "
        name1 += "\n"
        print(name1)
    else:
        print(line)
    count +=1



# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         print(movie.getText())
#         file.write(f"{movie.getText()}\n")