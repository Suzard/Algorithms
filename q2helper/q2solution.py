import re
from goody import irange
#Sumbitter edwardc6(Chen,Edward)
# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the file pattern.txt


def pages (page_spec : str) -> [int]: #result in ascending order (no duplicates)
    t = set()
    g = page_spec.split(',')
    pattern = "^([1-9][0-9]*)(-([1-9])([0-9])*((\/)([1-9])([0-9])*)?)?$"
    for i in g:
        if(re.match(pattern,i) == None):
            raise AssertionError
        else:
            if('-' in i):
                if('/' in i):
                    ko = i.split('-')
                    kot = int(ko[0])
                    jot = ko[1]
                    kotty = jot.split('/')
                    kotty1 = int(kotty[0])
                    kotty2 = int(kotty[1])
                    for i in range(kot, kotty1+1, kotty2):
                        t.add(int(i))
                else:
                    to = i.split('-')
                    z  = int(to[0])
                    za = int(to[1])
                    if(z > za):
                        raise AssertionError
                    else:
                        for i in range(z,za+1):
                            t.add(int(i))
                    
            else:
                t.add(int(i))
    godv = []
    for i in t:
        godv.append(i)
    godv.sort()
    return godv

def expand_re(pat_dict:{str:str}):
    for i in pat_dict:
        for t in pat_dict:
            pat_dict[t] = re.compile('#'+i+'#').sub('(' + pat_dict.get(i) + ')', pat_dict.get(t))
if __name__ == '__main__':
    print('Testing  examples of pages that returns lists')
    
if __name__ == '__main__':
    print('Testing  examples of pages that returns lists')
    
    print("  pages('5,3,9')        :", pages('5,3,9'))
    print("  pages('3-10,5-8,1-2') :", pages('3-10,5-8,1-2'))
    print("  pages(r'6-8,5-11/2,3'):", pages(r'6-8,5-11/2,3'))
    try:
        pages('5-3')
        print('  pages(5-3)            : Error: should have raised exception')
    except:
        print("  pages('5-3')          : raised exception (as it should)")
        
    print('\nTesting  examples of expand_re')
    pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary {'digit': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}
    
    pd = dict(integer       =r'[+-]?\d+',
              integer_range =r'#integer#(..#integer#)?',
              integer_list  =r'#integer_range#(?,#integer_range#)*',
              integer_set   =r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer'      : '[+-]?\\d+',
    #  'integer_range': '([+-]?\\d+)(..([+-]?\\d+))?',
    #  'integer_list' : '(([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*',   
    #  'integer_set'  : '{((([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'d': '(((correct)))',
    #  'c': '((correct))',
    #  'b': '(correct)',
    #  'a': 'correct',
    #  'g': '((((((correct))))))',
    #  'f': '(((((correct)))))',
    #  'e': '((((correct))))'
    # }

    print()
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
