from performance import Performance
from goody import irange
from graph_goody import random_graph, spanning_tree
from graph import Graph
#Submitter edwardc6(Chen,Edward)
# Put script here to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder
# random(100,lambda n : 10*n)
def create_random(n):
    global rand_graph
    rand_graph = random_graph(n, lambda n: 10*n)
def span_time(n):
    global rand_graph 
    spanning_tree(rand_graph)
z = 500
while True:
    n = z*2
    if(n == 256000):
        break;
    zoon = 'Spanning Tree of size {}'.format(str(n))
    jk = Performance(lambda: span_time(rand_graph), lambda: create_random(n),5,zoon) 
    jk.evaluate()
    jk.analyze()
    print()
    z = n
