import goody
#Submitter: edwardc6(Chen. Edward)
# Partner : cshenk(Shenk. Christian)
#Lab#4

def read_fa(file : open) -> {str:{str:str}}:
    b ={}
    for line in file:
        count = 0
        go = []
        zo = []
        a = line.rstrip().split(';')
        for i in a[1:]:
            count += 1
            if(count%2 != 0):
                go.append(i)
            else:
                zo.append(i)
        fad  = list(zip(go,zo))

        b[a[0]] = {t[0]: t[1] for t in fad}
    return b
            
        

def fa_as_str(fa : {str:{str:str}}) -> str:
    string = ""
    for i in sorted(fa):     
        z =  fa.get(i)
        string += "  {} transitions: {}\n".format(i,sorted([(i, z[i])for i in fa.get(i)], key = lambda x: x[0]))
        
    return string

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    g = []
    g.append(state)
    for i in inputs:
        try:
            
            g.append((i, fa[state][i]))
            state = fa[state][i]
        except:
            g.append((i, None))
            break
    return g

def interpret(fa_result : [None]) -> str:
    interpret_string = "Start state = {}\n".format(fa_result[0])
    for i in fa_result[1:]:
        if(i[1] == None):
            interpret_string += "  Input = {}; {}\n".format(i[0],"illegal input: simulation terminated")
            break
        interpret_string += "  Input = {}; new state = {}\n".format(i[0],i[1])
    interpret_string += "Stop state = {}\n".format(i[1])
    return interpret_string



if __name__ == '__main__':
    # Write script here
    efile = input("Enter file with finite automaton: ")
    print('\nFinite Automaton\n{}'.format(fa_as_str(read_fa(open(efile)))))
    file = input("Enter file with the start-state and input: ")
    print()
    for i in open(file):
        line = i.rstrip().split(';')
        print('Starting new simulation')
        t = interpret(process(read_fa(open(efile)), line[0],line[1:]))
        print(t)
        
    # For running batch self-tests
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
