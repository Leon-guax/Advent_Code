

def all_unique(item):
    return len(set(item)) == len(item)

def find_N_different(inp_puzzle, N):
    counter_1 =0
    while ( counter_1 <= len(inp_puzzle)):
        if all_unique(inp_puzzle[counter_1:counter_1+N]):
            break
        counter_1 +=1       
    return counter_1 +N


inp_puzzle = ''
with open('Day6_input.txt') as f:
    for line in f:
        print(find_N_different(line, 4), 4)
        print(find_N_different(line, 14), 14)

#%%
