
with open('Day6_input.txt','r') as f:
     data = [int(element) for element in f.read().split(',')] 
     
     
squids_grouped = [sum(int(value == x) for x in data) for value in range(0,9) ]
new_squids = [0 for idx in range(9)]    

final_time = 256


for idx_time in range(final_time):
    for idx_squids in range(1,9):
        new_squids[idx_squids -1] = squids_grouped[idx_squids]
    new_squids[8] = squids_grouped[0]
    new_squids[6] += squids_grouped[0]
    squids_grouped = new_squids[:]
        
print(sum(squids_grouped))    
        
        
