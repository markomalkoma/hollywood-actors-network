import json

with open('top_100_1.json') as file:
    top_100 = json.load(file)

film_actors = {}

for actor, films in top_100.items():
    films = list(set(films))
    for film in films:
        film_actors.setdefault(film,[]).append(actor)

from itertools import combinations as c

combos = []

for film, actors in film_actors.items():
    combos += list(c(actors, 2))

combos.sort()

print(combos[:100])
    
seting = list(set(combos))

total = []

for pair in seting:
    total.append(list(pair) + [combos.count(pair)])

print(total[:100])


c_0 = []
c_1 = []
c_2 = []

for triple in total:
    c_0.append(triple[0])
    c_1.append(triple[1])
    c_2.append(triple[2])

import pandas as pd

df = pd.DataFrame({'actor_1': c_0,
                   'actor_2': c_1,
                   'weight': c_2})

df.to_csv('top_100_1.csv', index=False)




















