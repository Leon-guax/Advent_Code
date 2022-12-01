import networkx as nx
import numpy as np
from itertools import islice

def k_shortest_paths(G, source, target, k, weight='weight'):
    return list(
        islice(nx.shortest_simple_paths(G, source, target, weight=weight), k)
    )


def weight_function(start, end, edge_attr):
    return int(cave[end[0]][end[1]])

cave = []
with open('Day15_input.txt','r') as f:
     for line in f:
        cave.append(list(line)[0:100]) 

graphed = nx.grid_2d_graph(100, 100, periodic=False, create_using=None)

for jdx in range(10):
    for idx in range(100):
        if idx >0:
            graphed.add_weighted_edges_from([((idx, jdx), (idx-1,jdx),int(cave[idx][jdx]))])
        if idx <100:
            graphed.add_weighted_edges_from([((idx, jdx), (idx+1,jdx),int(cave[idx][jdx]))])
        if jdx >0:
            graphed.add_weighted_edges_from([((idx, jdx), (idx,jdx-1),int(cave[idx][jdx]))])
        if jdx <99:
            graphed.add_weighted_edges_from([((idx, jdx), (idx,jdx+1),int(cave[idx][jdx]))])
            
            
best_paths =nx.shortest_simple_paths(graphed, (0,0), (99,99), weight='weight')

for path in k_shortest_paths(graphed, (0,0), (99,99), 2):
# for best_path in best_paths:
    cost =0
    for edge in path:

        cost += int(cave[edge[0]][edge[1]])

    print(cost)

#%%
# 1038 is too high
#%%
