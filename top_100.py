import requests
from bs4 import BeautifulSoup
import string

url = 'https://www.imdb.com/list/ls023242359/'

source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

actor_list=[]

driver = webdriver.Chrome()
driver.get(url)

blok = soup.find("div", {"class": "lister-list"})
actors = blok.find_all("h3", {"class": "lister-item-header"})

for actor in actors:
    name = actor.find("a")
    actor_list.append(name.get_text())

actors_names = list(map(lambda n:n.strip(string.punctuation+string.whitespace), actor_list))

print(actors_names)


with open("top_100.txt", "w") as f:
    for name in actors_names:
        f.write(name+'\n')


