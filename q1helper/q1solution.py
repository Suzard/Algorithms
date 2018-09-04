from collections import defaultdict
from math import atan2,sqrt
#Submitter edwardc6(Chen,Edward) Lab #1

def  compose(f : callable, g: callable):
    def compose2(x):
        a = g(x)
        b = f(a)
        return b
    return compose2
    

def self_compose(f : callable, n : int) -> callable:  
    if(n <0 ):
        raise AssertionError
    def self_compose2(x):
        
        for i in range(n):
            x = f(x)
        return x
    return self_compose2
    


def sorted1 (ps : {int:(int,int)}) -> [(int,(int,int))]:
    
        
    return sorted(ps.items(), key = lambda t: (t[1][0],-t[1][1]), reverse = False)

def sorted2 (ps : {int:(int,int)}) -> [(int,int)]:
    
    return sorted(ps.values(), key = lambda x: atan2(x[1],x[0]), reverse = False)

def sorted3 (ps : {int:(int,int)}) -> [int]:

    return sorted(ps, key = lambda x: atan2(ps[x][1], ps[x][0]), reverse = False)
    


def points (ps : {int:(int,int)}) -> [(int,int)]:
    return [ps[i] for i in sorted(ps)]


def first_quad (ps : {int:(int,int)}) -> {(int,int):float}:
    
    return {ps[i]: sqrt(ps[i][0]**2 + ps[i][1]**2) for i in ps if ps[i][0] >= 0and ps[i][1] >=0 }


def called(db : {str:{str:int}}) -> {str:int}:

    return {i:sum( list(db[i].values())) for i in db}

def got_called(db : {str:{str:int}}) -> {str:int}:
    b = defaultdict(int)
    for i in db:
        for g in db[i]:
            b[g] += db[i][g]
    return b

def invert(db : {str:{str:int}}) -> {str:{str:int}}:
    z = defaultdict(dict)
    for t,p in db.items():
        for i in p:
            z[i].update({t:db[t][i]})
    return z
    
if __name__ == '__main__':
    from goody import irange
   
    # Feel free to test other cases as well
     
    print('Testing compose')
    f = compose(lambda x : 2*x, lambda x : x+1)
    print( [(a,f(a)) for a in irange(0,10)] )
    g = compose(lambda x : x+1, lambda x : 2*x)
    print( [(a,g(a)) for a in irange(0,10)] )
       
    print('\nTesting self_compose')
    scl = [self_compose(lambda x : 2*x,i) for i in irange(0,6)]
    print([(1,f(1)) for f in scl])
           
    print('\nTesting sorted1')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(sorted1(ps))
#  
    print('\nTesting sorted2')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(sorted2(ps))
   
    print('\nTesting sorted3')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(sorted3(ps))
      
    print('\nTesting points')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(points(ps))
   
    print('\nTesting first_quad')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(first_quad(ps))
   
    print('\nTesting called')
    db = {'a':{'b':2,'c':1},'b':{'a':3,'c':1},'c':{'a':1,'d':2}}
    print(called(db))
       
    print('\nTesting got_called')
    db = {'a':{'b':2,'c':1},'b':{'a':3,'c':1},'c':{'a':1,'d':2}}
    print(called(db))
       
  
    print('\nTesting invert')
    db = {'a':{'b':2,'c':1},'b':{'a':3,'c':1},'c':{'a':1,'d':2}}
    print(invert(db))
#      
#     
#     print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()           





























