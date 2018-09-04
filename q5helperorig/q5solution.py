from functools import reduce # for peaks

def separate(p,l):
     
    if(l == []):
        return (l,l)
    else:
        if(p(l[0]) == True):
            t = []
            t.append(l[0])
            g= t + separate(p, l[1:])[0]
            return (g,separate(p,l[1:])[1])
        else:
            t = []
            t.append(l[0])
            g = t + separate(p, l[1:])[1]
            return (separate(p,l[1:])[0],g)
        

def is_sorted(s):
    if(s == [] or len(s) == 1):
        return True
     
    if(s[0]> s[1]):
        return False
    else:
        return is_sorted(s[1:])


def sort(l):
    #simple way to sort 
    if(l == []):
        return l
    else:
        g = []
        
        t = min(l)
        g.append(t)
        l.remove(t)
        return g + sort(l)
            
    
def compare(a,b):
    if(a == '' and  b == ''):
        return '='
    elif(a == '' and  b != ''):
        return '<'
    elif(b == '' and  a != ''):
        return '>'
    elif(a[0] > b[0]):
        return '>'
    elif(b[0] > a[0]):
        return '<'
    elif (b[0] == a[0]):
        return compare(a[1:], b[1:])
  
def triple(x,y): 
    ko = []
    zo = []
    for i in x:
        i.append(y)
    count = 0
    for t in x:
        count += 1
        if(count %3 != 0):
            ko.append(t)
        elif(count %3 == 0):
            zo.append(ko)
            print(zo)
            ko = []
            
    return zo

def peaks(alist):
    # from my quiz 4 solution 
    peaks = []
    g = iter(alist)
    z = next(g)
    t = -999
    while True:
        try:
          
            p = next(g)
            
            if(z> p and z >t):
                if(t  != -999):
                    #just to make sure t is less than z always so first value not taken
                    peaks.append(z)
                else:
                    pass
            #t saves previous value
            t = z
            #after calculating current now after becomes current
            z = p
        except StopIteration:
            return peaks





if __name__=="__main__":
    import predicate,random,driver
    from goody import irange
    
#     print('Testing separate')
    print(separate(predicate.is_positive,[]))
    print(separate(predicate.is_positive,[1, -3, -2, 4, 0, -1, 8]))
    print(separate(predicate.is_prime,[i for i in irange(2,20)]))
    print(separate(lambda x : len(x) <= 3,'to be or not to be that is the question'.split(' ')))
      
    print('\nTesting is_sorted')
    print(is_sorted([]))
    print(is_sorted([1,2,3,4,5,6,7]))
    print(is_sorted([1,2,3,7,4,5,6]))
    print(is_sorted([1,2,3,4,5,6,5]))
    print(is_sorted([7,6,5,4,3,2,1]))
     
    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = [i+1 for i in range(30)]
    random.shuffle(l)
    print(l)
    print(sort(l))
#     
#     print('\nTesting compare')
#     print(compare('','abc'))
#     print(compare('abc',''))
#     print(compare('',''))
#     print(compare('abc','abc'))
#     print(compare('bc','abc'))
#     print(compare('abc','bc'))
#     print(compare('aaaxc','aaabc'))
#     print(compare('aaabc','aaaxc'))
#     
#     print('\nTesting triple and peaks')
#     print(triple([[]],'a'))
#     print(triple([['a']],'b'))
#     print(triple([['a','b']],'c'))
#     print(triple([['a','b','c']],'d'))
#     print(triple([['a','b','c'],['b','c','d']],'e'))
#     print(triple([['a','b','c'],['b','c','d'],['c','d','e']],'f'))
#     
#     print(peaks([0,1,-1,3,8,4,3,5,4,3,8]))
#     print(peaks([5,2,4,9,6,1,3,8,0,7]))
#     print(peaks([1,2,3,4,5]))
#     print(peaks(int(predicate.is_prime(p)) for p in irange(1,20)))
#     
    driver.default_file_name = 'bsc.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
    
