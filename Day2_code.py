depth = 0
hor_dist = 0
with open('Day2_input.txt') as f:
     for line in f:
        if line.split()[0] == 'forward':
            hor_dist += int(line.split()[1])
            
        elif line.split()[0] == 'down':
            depth += int(line.split()[1]) 
           
        elif line.split()[0] == 'up':
            depth -= int(line.split()[1]) 


ans = depth * hor_dist
print(ans)