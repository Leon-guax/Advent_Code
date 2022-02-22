data = []
with open('Day1_input.txt') as f:
     for line in f:
        data.append([int(v) for v in line.split()]) 

data_diff =[ data[idx+1][0] - data[idx][0] for idx in range(0, len(data)-1) ]
pos_count_single = len(list(filter(lambda x: (x > 0), data_diff)))
print(pos_count_single)

diff_triplet = [ data[idx+3][0] - data[idx][0] for idx in range(0, len(data)-3) ]
pos_count_triplets = len(list(filter(lambda x: (x > 0), diff_triplet)))
print(pos_count_triplets)