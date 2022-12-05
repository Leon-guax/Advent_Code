import re

ship9000 =[[],
       ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
       ['Q', 'R', 'B'],
       ['B', 'Z', 'T', 'Q', 'P', 'M', 'S'],
       ['D', 'V', 'F', 'R', 'Q', 'H'],
       ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'],
       ['W', 'R', 'T', 'Z'],
       ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'],
       ['R', 'N', 'F', 'H', 'W'],
       ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']]

ship9001 =[[],
       ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
       ['Q', 'R', 'B'],
       ['B', 'Z', 'T', 'Q', 'P', 'M', 'S'],
       ['D', 'V', 'F', 'R', 'Q', 'H'],
       ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'],
       ['W', 'R', 'T', 'Z'],
       ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'],
       ['R', 'N', 'F', 'H', 'W'],
       ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']]

with open('Day5_input.txt') as f:
    for line in f:
       command = [int(idx) for idx in re.split('move | from | to ', line.replace('\n',''))[1:]]
       ship9001[command[2]] += ship9001[command[1]][-command[0]:]
       for nr_crates in range(command[0]):
           ship9000[command[2]].append(ship9000[command[1]].pop())
           ship9001[command[1]].pop()
           
                        
final_order9000 =''
final_order9001 =''
for idx in range(1,10):
    final_order9000 = final_order9000 + ship9000[idx][-1] 
    final_order9001 = final_order9001 + ship9001[idx][-1] 
    
print(final_order9000)
#BZLVHBWQF
print(final_order9001)

#%%
