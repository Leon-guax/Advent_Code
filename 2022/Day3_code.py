import string
alphabet = list(string.ascii_letters)

prio_dict = {}

for L, N in zip(alphabet, range(1, 52+1)):
    prio_dict[L] = N
    
prio_sum =0
matching_badge_sum =0
with open('Day3_input.txt') as f:
     for line, lineNr in zip(f, range(1, 300+1)):
         line = line.replace('\n',"")
         
         if lineNr % 3 ==1:
             firstElfLine = line
         elif lineNr % 3 ==2:
             secondElfLine = line
         elif lineNr % 3 ==0:
             thirdElfLine = line
             matchingBadge = ''.join(set(firstElfLine).intersection(secondElfLine).intersection(thirdElfLine))
             matching_badge_sum += prio_dict[matchingBadge]
         
         
         ruck1 = line[:int((len(line)-1)/2)+1]
         ruck2 = line[int((len(line)-1)/2)+1:]

         #print(ruck1,'|', ruck2)
         #print(len(ruck1), len(ruck2))
         doubleL = ''.join(set(ruck1).intersection(ruck2))
         prio_sum += prio_dict[doubleL]



print(prio_sum)
print(matching_badge_sum)

#%%
