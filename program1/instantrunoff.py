import goody
from collections import defaultdict
#Submitter: edwardc6(Chen, Edward)
# Partner : cshenk(Shenk, Christian)
#Lab#4
def read_voter_preferences(file : open):
    read_file = file
    source_node_dict = {}
    for line in read_file:
        a = line.rstrip().split(';')
        source_node_dict[a[0]] = a[1:]
    return source_node_dict

def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    string = ""
    for i in sorted(d, key= key, reverse= reverse):        
        string += "  {} -> {}{}".format(i,str(d.get(i)),'\n')
        
    return string
        
def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    vote_count = defaultdict(int)
    for i in cie:
        vote_count[i] = 0
    for v in vp:
        for g in vp.get(v):
            if g in cie:
                vote_count[g] += 1
                break
    return vote_count

def remaining_candidates(vd : {str:int}) -> {str}:
    d = {i for i in vd if vd.get(i) != min(vd.values())}
    return d

def run_election(vp_file : open) -> {str}:
    voter_preferences = read_voter_preferences(vp_file)
    print('Voter Preferences')
    print(dict_as_str(voter_preferences))
    count = 0
    remaining_candidate = voter_preferences
    for i in voter_preferences:
        candidate_list = voter_preferences.get(i)
        break;
    while True:
        if(count == 0):
            count += 1
            gd = evaluate_ballot(voter_preferences, candidate_list)
            print("Vote count on #{} with candidates (alphabetically) = ".format(count),\
                  {i for i in sorted(gd, reverse = False)})
            for i in sorted(gd, reverse = False):
                print("  {} -> {}".format(i,gd.get(i)))
                
            print()
        
            print("Vote count on #{} with candidates (numerically) = ".format(count),\
                  {i for i in sorted(gd, key = lambda x: gd.get(x), reverse = True)})
            for i in sorted(gd, key = lambda x: gd.get(x), reverse = True):
                print("  {} -> {}".format(i, gd.get(i)))
                
            print()
                
        else:
            count += 1
            p = evaluate_ballot(voter_preferences, candidate_list)
            remaining_candidate = remaining_candidates(p)
            candidate_list = remaining_candidate
            z = evaluate_ballot(voter_preferences, candidate_list)
            if(len(remaining_candidate) ==1 or len(remaining_candidate) == 0):
                if(len(remaining_candidate) == 0):
                    print('There is a tie')
                    return remaining_candidate
                else:
                    print('Winner is {}'.format(remaining_candidate))
                    return remaining_candidate
            print("Vote count on #{} with candidates (alphabetically) = ".format(count),\
                  {i for i in sorted(z, reverse = False)})
            for i in sorted(z, reverse = False):
                print("  {} -> {}".format(i,z.get(i)))
            print()
            print("Vote count on #{} with candidates (numerically) = ".format(count),\
                  {i for i in sorted(z, key = lambda x: z.get(x), reverse = True)})
            for i in sorted(z, key = lambda x: z.get(x), reverse = True):
                print("  {} -> {}".format(i, z.get(i)))   
                
            print()          
    
    
if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    z = input("Enter file with voter preferences: ")
    print()
    run_election(open(z))
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
