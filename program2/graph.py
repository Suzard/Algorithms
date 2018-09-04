# Define a special exception for use with the Graph class methods
# Use like any exception: e.g., raise GraphError('Graph.method...error indication...')
from collections import defaultdict
class GraphError(Exception):
    pass # Inherit all methods, including __init__
 
 
class Graph:
    # HELPER METHODS: used for checking legal arguments to methods below
    def legal_tuple2(self,t):
        return type(t) is tuple and len(t) == 2 and\
               type(t[0]) is str and type(t[1]) is str

    def legal_tuple3(self,t,z):
        return type(t) is tuple and len(t) == 3 and\
               type(t[0]) is str and type(t[1]) is str and z(t[2])
        
 
    # __str__ and many bsc tests use the name self.edges for the outer/inner-dict.
    # So __init__ should use self.edges for the name for this dictionary
    # self should store NO other attributes: compute all results from self.edges ONLY
    # Each value in the edges tuple can be either a 
    #   (a) str = origin node
    #   (b) 3-tuple = (origin node, destination node, edge value) 
    def __init__(self,legal_edge_value_predicate,*edges):
        self.f = legal_edge_value_predicate
        self.edge = edges 
        self.edges = defaultdict(dict)
        g = []
        for i in edges:
            if(self.legal_tuple3(i, legal_edge_value_predicate) == True ):
                if((i[0],i[1]) in g):
                    raise GraphError
                else:
                    if(i[0] in self.edges):
                        self.edges[i[0]].update({i[1]:i[2]})
                    else:
                        self.edges[i[0]] = {i[1]:i[2]}
                    if(i[1] not in self.edges):
                        self.edges[i[1]] = {}
                        
                    g.append((i[0], i[1]))
                    g.append(i[0])
                    g.append(i[1])
                    

            elif(type(i) == str and len(i) == 1):
                if(i in g):
                    raise GraphError 
                else:
                    self.edges[i] = {}
                    g.append(i)
            else:
                raise GraphError
    def copy(self):
        z = defaultdict(dict)
        for i in self.edges: 
            if(self.edges[i] == {}):
                z[i].update({})
                
            for t in self.edges[i]:
                z[i].update({t:self.edges[i][t]})
        return z 
                
    def __str__(self):
        
        string = '\nGraph:\n'
        for i in sorted(self.edges):
            string += "  {}:".format(i)
            
            if(self.edges[i] != dict()):
            
                for z in sorted(self.edges[i]):
                    string += ' {}({}),'.format(z, self.edges[i][z])
                string = string[0:-1]
            string += '\n'
        return string[0:-1]
    def __getitem__(self,item):
        if(type(item) == str):
            if(item not in self.edges):
                raise GraphError
            
            return self.edges[item]
            
        elif(self.legal_tuple2(item) == True):
            for (i,v) in self.edges.items():

                if(item[0] == i and item[1] in v):
                    return v[item[1]]
                
            raise GraphError
                    
            
            
        else:
            raise GraphError 
    def __setitem__(self,item, value):
        if(type(value) != int):
            raise GraphError
        if(self.legal_tuple2(item) == True):
            for (i,v) in self.edges.items():

                if(item[0] == i and item[1] in v):
                    self.edges[item[0]][item[1]] = value
                    break 
            if(item[1] not in self.edges):
                self.edges[item[1]] = {}
                self.edges[item[0]].update({item[1]:value})
            else:
                self.edges[item[0]].update({item[1]:value})
        else:
            raise GraphError
    def node_count(self):
        g = set()
        for i in self.edges:
            if(self.edges[i] != {}):
                for t in self.edges[i]:
                    g.add(t)
            g.add(i)
        return len(g)
    def __len__(self):
        count = 0
        for i in self.edges:
            if(self.edges[i] != {}):
                for t in self.edges[i]:
                    count += 1
        return count
    def out_degree(self, node):
        if(type(node) != str or node not in self.edges):
            raise GraphError
        count = 0
        for i in self.edges:
            if(self.edges[i] != {} and i == node):
                for t in self.edges[i]:
                    count += 1
        return count
    def in_degree(self,node):
        if(type(node) != str or node not in self.edges):
            raise GraphError
        count = 0
        for i in self.edges:
            if(self.edges[i] != {}):
                for t in self.edges[i]:
                    if(t == node):
                        count += 1
        return count
    def __contains__(self,node):
        if(type(node) == str):
            return node in self.edges
        elif(self.legal_tuple2(node) == True):
            for (i,v) in self.edges.items():

                if(node[0] == i and node[1] in v):
                    return True
            return False
        elif(self.legal_tuple3(node, lambda x: type(x) == int) == True):
            
                for (i,v) in self.edges.items():

                    if(node[0] == i and node[1] in v and node[2] == v[node[1]]):
                        return True
                return False
            
        else:
            raise GraphError
    def __delitem__(self, item):
        z = defaultdict(dict)
        if(self.legal_tuple2(item) == True):
            
            for (i,v) in self.edges.items():
                if(v == {}):
                    z[i].update({})
                for value in v:
                    if(item[0] == i and value == item[1]):
                        if(len(self.edges[i]) == 1):
                            z[i].update({})
                    else:
                        z[i].update({value:v[value]})

        elif(type(item) == str):
            for (i,v) in self.edges.items():
                if(i == item):
                    pass
                else:
                    if(v == {}):
                        z[i].update({})
                    for value in v:
                        
                        if(value == item):
                            if(len(self.edges[i]) == 1):
                                z[i].update({})
                        else:
                            z[i].update({value:v[value]})
        else:
            raise GraphError                  
        self.edges = z
    def __call__(self,item):
        z = dict()
        if(item not in self.edges):
            raise GraphError
        for (i,v) in self.edges.items():
            for g in v:
                if(g == item):
                    z[i] = v[g]
                    
        return z
    def clear(self):
        self.edges = {}
                    
    def dump(self, file, sep,type = str):
        string = ''
        for i in sorted(self.edges):

            string += type(i)
            for t in sorted(self.edges[i]):
                string += type(sep)
                string += type(t)
                string += type(sep)
                string += type(self.edges[i][t])
            string += '\n'
        file.write(string)    
    def load(self, file, sep, type = int):
        z = defaultdict(dict)
        for line in file:
            j = line.strip('\n').split(sep)
            if(len(j) == 1):
                z[j[0]].update({})
            count = 0
            t = []
            lo = []
            for lk in j[1:]:
                if(count %2 == 0):
                    t.append(lk)
                else:
                    lo.append(lk)
                count += 1
            for (zo, ko) in zip(t,lo):
                z[j[0]].update({zo:type(ko)})
                if(zo not in z):
                    z.update({})
                    
                
        self.edges = z 
    def reverse(self):
        f = Graph(self.f)
        z = defaultdict(dict)
        for i in self.edges:
            if(self.edges[i] == {} or i not in z):
                z[i].update({})
            for t in self.edges[i]:
                z[t].update({i:self.edges[i][t]})
        f.edges = z
        return f
                
        
    def natural_subgraph(self, *args):
        g = defaultdict(dict)
        grap = Graph(self.f)
        for i in args:
            if(type(i) != str):
                raise GraphError
            for t in self.edges:
                if(i not in g and i in self.edges):
                    g[i].update({})
                for z in self.edges[t]:
                    if(z  in args and t in args):
                        g[t].update({z:self.edges[t][z]})
        grap.edges = g
        return grap
    def __iter__(self):
        z = []
        for i in sorted(self.edges):
            if(self.edges[i] == {} and i not in z):
                yield i 
            for t in sorted(self.edges[i]):
                z.append(i)
                z.append(t)
                yield (i,t,self.edges[i][t])
    def __eq__(self,right ):
        return self.edges == right.edges 
    def __neq__(self,right):
        return self.edges != right.edges

    def __le__(self,right):
        for i in self.edges:
            if(self.edges[i] == {}):
                if(right.edges.get(i) != {}):
                   return False
            for t in self.edges[i]:
                if(i in right.edges):
                    if(t in right.edges[i]):
                        if(right.edges[i][t] != self.edges[i][t]):
                            return False
                    else: 
                        return False 
                else: 
                    return False
        return True
    def __add__(self,right):
        grap = Graph(lambda x: type(x) == int)
        if(type(right) == Graph):
            z = self.copy()
            for i in right.edges:
                if(i not in z):
                    z[i].update(right.edges[i])
 
                for tot in right.edges[i]:
                    if(z[i].get(tot) == None):
                        z[i].update({tot:right.edges[i][tot]})
            grap.edges = z
            return grap
                    

        elif(type(right) == str):
            z = self.copy()
 
            if(right not in z):
                z[right].update({})
            grap.edges = z
            return grap
        elif(self.legal_tuple3(right, self.f) == True):
            z = self.copy()
            z[right[0]].update({right[1]:right[2]})
            if(right[0] not  in z):
                z[right[0]].update({})
            if(right[1] not in z):
                z[right[1]].update({})
            grap.edges = z
            return grap
        else: 
            raise GraphError

    def __radd__(self,right):
        return self + right
    def __iadd__(self,right):
        z = self.__add__(right)
        self.edges = z.edges
        return self
    def __setattr__(self, right, value):
        #screwed up this part because you cant set self.edges to something
        #that confuses this part. What you must do is use directly 
        #self.edges and not set it equal to naything
        self.__dict__[right] = value
        
if __name__ == '__main__':
    #Put code here to test Graph before doing bsc test; for example
    #g = Graph( (lambda x : type(x) is int), ('a','b',1),('a','c',3),('b','a',2),('d','b',2),('d','c',1),'e')
#     print(g)
#     print(g['a'])
#     print(g['a','b'])
#     print(g.node_count())
#     print(len(g))
#     print(g.out_degree('c'))
#     print(g.in_degree('a'))
#     print('c' in g)
#     print(('a','b') in g)
#     print(('a','b',1) in g)
#     print(g('c'))
#     print(g.reverse())
#     print(g.natural_subgraph('a','b','c'))
#     print()    
     
    import driver
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
