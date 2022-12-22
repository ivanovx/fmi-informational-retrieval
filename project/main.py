import re
import json

CLEAN_HTML = re.compile('<.*?>') 

file = open('../dataset/bg-movies.json', 'r', encoding='utf-8')

movies = json.loads(file.read())

for movie in movies:
    title = movie['title']
    description = ''

    for desc in movie['description']:
        clear = re.sub(CLEAN_HTML, '', desc)

        description += clear

    print('-----------')
    print(title)
    print(description)
    print('-----------')