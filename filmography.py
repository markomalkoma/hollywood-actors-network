def urls(actor, t):
    base = 'https://en.wikipedia.org/wiki/'
    if t == 0:
        url = base + 'List_of_' + actor + '_performances'   
    elif t == 1:
        url = base + actor + '_filmography'
    elif t == 2:
        url = base + actor + '_on_screen_and_stage'       
    elif t == 3:       
        url = base + actor
    
    return url

def selector(hed, data):
    tables = []
    for h in data:
        try:
            hey = h.find('span')
            if hey.get_text() == 'Film' or 'Feature films' or 'Films':
                for s in h.next_siblings:
                    if s.name == 'table':
                        tables.append(s)
                    if s.name == hed:
                        break
        except:
            pass
        
    return tables


def filmography(actor, t):
    print(actor)
    url = urls(actor, t)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    data_2 = soup.find_all("h2")
    data_3 = soup.find_all("h3")
    data_4 = soup.find_all("h4")
    tables = selector('h2', data_2)
    if len(tables) == 0:
        tables = selector('h3', data_3)
    if len(tables) == 0:
        tables = selector('h4', data_4)
    titles = []
    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            i_s = row.find_all('i')
            for i in i_s:
                links = i.find_all('a')
                for link in links:
                    try:
                        title = link.get('title')
                        titles.append(title)
                    except:
                        print(actor)
                        pass

    titles = [title for title in titles if title]

    if len(titles) == 0:
        t += 1

        if t < 4:
            return filmography(actor, t)

    return titles


if __name__ == '__main__':
    
    import requests
    from bs4 import BeautifulSoup

    with open("top_100.txt", "r") as f:
        actors = [line.rstrip('\n') for line in f]

    top_100 = {}

    for actor in actors:
        try:
            top_100[actor] = filmography(actor, 0)
        except:
            print(actor)

    k=0    
    for actor, films in top_100.items():
        k+=1
        print(k, actor, films[:1])

    import json
    
    with open('top_100.json', 'w') as f:
        json.dump(top_100, f)
    
    




    
