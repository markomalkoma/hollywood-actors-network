from itertools import combinations as CMB

with open("top_100_1.txt", "r") as f:
    actors = [line.rstrip('\n') for line in f]

def read_graph(actors):

    import pandas as pd
    
    df = pd.read_csv('top_100_1.csv')
    
    n_pairs = len(df) - 100
    n_actors = len(actors)

    graph = dict((i, []) for i in actors)
    
    for j in range(1, n_pairs):
        
        f = df.iloc[j]
        u = f['actor_1']
        v = f['actor_2']
        graph[u].append(v)
        graph[v].append(u)
        
    return graph

graph = read_graph(actors)

def search(graph, used, combos):
    combinations = []
    for c in combos:
        for actor in graph[c[-1]]:
            if actor not in used:
                s = c[:]
                s.append(actor)
                combinations.append(s)
                used.append(actor)
            else:
                continue
    if len(combinations) == 0:
        return combos
    else:
        combos = combinations
        return search(graph, used, combos)

actor_furthest = {}
for_pie = []

for actor in actors:
    furthest = []
    seed = actor
    used = [seed]
    combos = [[seed]]
    find = search(graph, used, combos)
    for group in find:
        furthest.append(group[-1])
    actor_furthest[actor] = furthest
    l_find = len(find[0])
    for_pie.append((l_find, actor))
    print(seed, l_find)

for_pie.sort()

group_3 = []
group_4 = []

for name in for_pie:
    if name[0] == 3:
        group_3.append(name[1])
    else:
        group_4.append(name[1])
        
print(group_3)
print(group_4)

actor_seed_importance = []

for actor in actors:
    k = 0
    for key, val in actor_furthest.items():
        if actor in val:
            k += 1
    actor_seed_importance.append((k, actor))

actor_seed_importance.sort(reverse = True)

print(actor_seed_importance)

def centroids(actors, graph, k):
    combinations = list(CMB(actors, k))
    valued_combos = []
    for combo in combinations:
        combo_actors = []
        for node in combo:
            combo_actors += graph[node]
        score = 0
        for actor in set(combo_actors):
            comited = 0
            for node in combo:
                if actor in graph[node]:
                    comited += 1
            if comited == 1:
                score -= 1
            else:
                score += 1
        valued_combos.append((score, combo))

    valued_combos.sort()

    return valued_combos[:200]
                
print(centroids(actors, graph, 4))           




    
