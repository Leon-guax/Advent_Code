data = []
amount_cal =0
with open('Day1_input.txt') as f:
     for line in f:
         if line !="\n":
             amount_cal += int(line)    
         else:
            data.append(amount_cal)
            amount_cal =0
            
data.sort()
print(data[-1])


print(sum(data[-3:]))

#data_diff =[ data[idx+1][0] - data[idx][0] for idx in range(0, len(data)-1) ]
#pos_count_single = len(list(filter(lambda x: (x > 0), data_diff)))
#print(pos_count_single)

#diff_triplet = [ data[idx+3][0] - data[idx][0] for idx in range(0, len(data)-3) ]
#pos_count_triplets = len(list(filter(lambda x: (x > 0), diff_triplet)))
#print(pos_count_triplets)