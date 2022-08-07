
def number_of_links(df, actor, generations):
    for _ in range(generations):
        f = df.loc[(df.actor_1 == actor) | (df.actor_2 == actor)]
        actors = list(set(list(f['actor_1']) + list(f['actor_2'])))
    print(actor, len(actors))
    return len(actors)


def draw(actors, n_of_links, border):
    
    plt.figure(str(border))
    plt.style.use('seaborn-darkgrid')
    plt.rcParams.update({'font.size': 10})
    title = " Number of links"
    plt.title(title, fontsize = 12)    
    return plt.barh(actors[border[0]:border[1]], n_of_links[border[0]:border[1]])


if __name__ == '__main__':
    
    import pandas as pd
    df = pd.read_csv('top_100_1.csv')
    
    with open("top_100_1.txt", "r") as f:
        actors = [line.rstrip('\n') for line in f]

    actor_n_of_links = []
    actor_n_of_links_dict = {}

    
    for actor in actors:
        len_links = number_of_links(df, actor, 1)
        actor_n_of_links.append((len_links, actor))
        actor_n_of_links_dict[actor] = len_links
        
    actor_n_of_links.sort()
    actors = [i[1] for i in actor_n_of_links]
    n_of_links = [i[0] for i in actor_n_of_links]

    actor_n_of_links.sort(reverse = True)

    for links_actor in actor_n_of_links:
        print(links_actor[0], links_actor[1])

    import json

    with open('top_100_1.json') as file:
        filmography = json.load(file)

    importance = []
    len_filmography = []
    for actor in actors:
        len_f = len(filmography[actor])
        len_filmography.append((len_f, actor))
        score = (actor_n_of_links_dict[actor] - 1)/len_f
        score = round(score, 2)
        importance.append((score, actor))

    importance.sort(reverse = True)
    len_filmography.sort(reverse = True)

    for actor in len_filmography:
        print(actor[0], actor[1])

    for actor in importance:
        print(actor[0], actor[1])

    borders = [(0,33), (33,66), (66,99)]

    from matplotlib import pyplot as plt

    for border in borders:
        draw(actors, n_of_links, border)

    plt.show()
    

