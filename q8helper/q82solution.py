import cProfile
from graph_goody import random_graph,spanning_tree
import pstats
#Submitter edwardc6(Chen,Edward)
# Put script here to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder
def create_random(n):
    global rand_graph
    rand_graph = random_graph(n, lambda n: 10*n)
def span_time(n):
    global rand_graph 
    spanning_tree(rand_graph)
create_random(50000)
cProfile.run('span_time(rand_graph)','profile50k')
p = pstats.Stats('profile50k')
p.sort_stats('calls').print_stats(19)
create_random(100000)
cProfile.run('span_time(rand_graph)','profile100k')
g = pstats.Stats('profile100k')
g.sort_stats('time').print_stats(19)