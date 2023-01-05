import re
import json

CLEAN_HTML = re.compile('<.*?>') 

file = open('../dataset/bg-movies.json', 'r', encoding='utf-8')

movies = json.loads(file.read())

for movie in movies:
    title: str = movie['title']
    description = movie['description']

    es.index(index='bgmovies', document=movie)