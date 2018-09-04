import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query
#Submitter: edwardc6(Chen, Edward)
# Partner : cshenk(Shenk, Christian)
#Lab#4

def all_prefixes(fq : (str,)) -> {(str,)}:
    t = set()
    count = 0
    for i in fq:
        count += 1
        t.add(fq[0:count])
    return t
        
def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    t = all_prefixes(new_query)
    for i in t:
        prefix[i].add(new_query)
    query[new_query] += 1

def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    p = defaultdict(set)
    q = defaultdict(int)
    for i in open_file:
        g = i.split()
        add_query(p,q,tuple(g))
    return p,q
        
def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    string = "" 
    for i in sorted(d, key = key, reverse = reverse):
        string += '  {} -> {}\n'.format(i, d.get(i))
    return string   

def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    t = []
    z = []
    if(a_prefix not in prefix):
        return []
    for i in prefix[a_prefix]:
        t.append((i,query[i]))
    g = sorted(t, key = lambda x: (-x[1],x[0]), reverse = False)
    count  = 0
    for i in g:
        if(count == n):
            break
        z.append(g[count][0])
        count += 1
    return z
# Script

if __name__ == '__main__':
    # Write script here
    a = input("Enter file with full queries: ")
    g = read_queries(open(a))
    print()
    print('Prefix dictionary: ')
    print(dict_as_str(g[0], key = lambda x: (len(x),x)))
    print('Query dictionary:')
    print(dict_as_str(g[1], key = lambda x: (g[1].get(x), -len(x)), reverse = True))
    while True:
        a = input('Enter prefix (or quit): ')
        if(a == 'quit'):
            break
        print('  Top 3 (at most) full queries = {}'.format(top_n(tuple(a.split()), 3, g[0], g[1])))
        print()
        b = input('Enter full query (or quit): ')
        if(b == 'quit'):
            break
        add_query(g[0], g[1], tuple(b.split()))
        print(dict_as_str(g[0], key = lambda x: (len(x),x)))
        print('Query dictionary:')
        print(dict_as_str(g[1], key = lambda x: (g[1].get(x), -len(x)), reverse = True))
   
        
     
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
