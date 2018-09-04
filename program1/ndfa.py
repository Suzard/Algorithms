import goody
#Submitter: edwardc6(Chen, Edward)
# Partner : cshenk(Shenk, Christian)
#Lab#4
def read_ndfa(file : open) -> {str:{str:{str}}}:
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
        b.setdefault(a[0], {})
        for i in fad:
            b[a[0]].setdefault(i[0],set()).add(i[1])
    return b

def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    string = ""
    for i in sorted(ndfa):
        string += "  {} transitions: {}\n".format(i,sorted([ (d,sorted(list(c)))for d,c in ndfa.get(i).items()]))
    return string

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    p = []
    p.append(state)
    sd = set()
    sd.add(state)
    for i in inputs:
        tz = set()
        kora = []
        kor = set()
        for po in sd:
            if(ndfa[po].get(i) == None):
                pass
            else:
                for kj in ndfa[po].get(i):
                    tz.add(kj)
                    kora.append(ndfa[po][i])
        for tod in kora:
            for tood in tod:
                kor.add(tood)
        p.append((i,kor))
        if(kor == set()):
            break
        sd = tz
    return p

def interpret(result : [None]) -> str:
    string = "Start state = {}\n".format(result[0])
    for i in result[1:]:
        string += "  Input = {}; new possible states = {}\n".format(i[0], sorted(list(i[1])))    
    string += "Stop state(s) = {}\n".format(sorted(list(i[1])))
    return string

if __name__ == '__main__':
    # Write script here
    file1 = input("Enter file with non-deterministic finite automaton: ")
    print()
    print('Non-Deterministic Finite Automaton')
    print(ndfa_as_str(read_ndfa(open(file1))))
    file2 = input("Enter file with start-state and input: ")
    print()
    for line in open(file2):
        a = line.rstrip().split(';')
        print('Starting new simulation')
        print(interpret(process(read_ndfa(open(file1)), a[0], a[1:])))
#         print(proces)
        #print(interpret(proces))
    # For running batch self-tests
    
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
