import networkx as nx
import pandas as pd

df = pd.read_csv('top_100_1.csv')

seed = 'Joaquin Phoenix Cate Blanchett Michael B. Jordan Michael Keaton'
generations = 4

actors = ['Joaquin Phoenix', 'Cate Blanchett', 'Michael B. Jordan', 'Michael Keaton']


f = df.loc[(df.actor_1.isin(actors)) | (df.actor_2.isin(actors))]

G = nx.from_pandas_edgelist(f, source = 'actor_1', target = 'actor_2', edge_attr = 'weight')

#nx.draw(G)

import pyvis

from pyvis.network import Network


net = Network(bgcolor='#222222', font_color='white')

net.from_nx(G)

name = seed + '_' + str(generations) + '.html'

net.show(name)
