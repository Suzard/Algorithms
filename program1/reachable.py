import goody
import prompt
from collections import defaultdict
#Submitter: edwardc6(Chen, Edward)
# Partner : cshenk(Shenk, Christian)
#Lab#4

def read_graph(file : open) -> {str:{str}}:
    read_file = file
    source_node_dict = {}
    for line in read_file:
        a = line.rstrip().split(';')
        if a[0] not in source_node_dict:
            d = set()
            d.add(a[1])
            source_node_dict[a[0]] = d
        else:
            b = source_node_dict.get(a[0])
        
            b.add(a[1])
            source_node_dict[a[0]] = b
    return source_node_dict


def graph_as_str(graph : {str:{str}}) -> str:
    string = ""
    for i in sorted(graph):
        string += "  {} -> {}{}".format(i,str(sorted(list(graph.get(i)))),'\n')
    return string
        
def reachable(graph : {str:{str}}, start : str) -> {str}:
    
    reached_nodes = set()
    exploring_list = [start]
    while True:
        if(exploring_list == []):
            return reached_nodes
        g = exploring_list.pop()
        reached_nodes.add(g)
        try:
            for i in graph.get(g):
                if i not in reached_nodes:
                    exploring_list.append(i)
        except:
            pass
if __name__ == '__main__':
    while True:
        try:
            user_graph = input("Enter file with graph: ")
            reading_graph = open(user_graph)
            graph = read_graph(reading_graph)
            if(type(graph) == dict):
                break
        except:
            print("Invalid graph error")
        
        
    print("\nGraph: source -> {destination} edges")
    print(graph_as_str(graph))
    while True:
        try:
                
            user_node = input("Enter a starting node name: ")
            if(user_node not in graph):
                raise Exception

            print("From {} the reachable nodes are {}\n".format(user_node,reachable(graph, user_node)))
                
                
        except:
            if(user_node == 'quit'):
                break
            print("  Entry Error: {}; Illegal: not a source node".format(user_node))
            print("  Please enter a legal string")
            print()
        
    # Write script here
              
    # For running batch self-tests
    
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
