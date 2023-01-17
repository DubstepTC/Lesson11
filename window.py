import json
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
soup = response.json()

# Запись  "js.json"
with open("js.json", "w+", encoding = 'utf-8') as file:
    json.dump(soup,file, indent = 5)

# Функция которая нужна для чтения файла  "js.json"
def read(filename)   :
    with open("js.json", "r", encoding = 'utf-8') as file:
            return json.load(file)

# Вывод инф из файла "js.json"
fl = read("js.json")
for i in range(len(fl)) :
        print(str(i) + " - "  + fl[i]["title"])