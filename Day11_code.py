import numpy as np

def numbers_biggr_9(matrix):
    biggr_9 = [[False for idx in range(len(matrix[0]))] for jdx in range(len(matrix))] 
    high_val = np.where(matrix >9)

    for idx, jdx in zip(high_val[0], high_val[1]):
        biggr_9[idx][ jdx] = True
        
    return biggr_9

def find_neighbours(matrix, idx, jdx):
    neighbour =[[False for idx in range(len(matrix[0]))] for jdx in range(len(matrix))] 
    for hor in range(-1,2):
        for ver in range(-1,2):
            if ((idx+ hor >=0) and (idx+hor < len(matrix[0])) and 
                (jdx +ver >=0) and (jdx+ver < len(matrix))):
                neighbour[idx+hor][jdx+ver]= True

    return neighbour
    
def energize_neighbours(matrix, neighbours):
    for idx in range(len(matrix)):
        for jdx in range(len(matrix[0])):
            if neighbours[idx][jdx]:
                matrix[idx][jdx] +=1
    return matrix

def flash_energize_count(matrix, flashing_matrix):
    nr_flashes =0
    for idx in range(len(matrix)):
        for jdx in range(len(matrix[0])):
            if matrix[idx][jdx]>9:
                nr_flashes +=1
                matrix[idx][jdx] =-100
                flashing_matrix[idx][jdx] = True
                neighbours = find_neighbours(matrix, idx, jdx)
                matrix = energize_neighbours(matrix, neighbours)
    return (flashing_matrix, matrix, nr_flashes)         
  
def reset_counter(matrix, flashing_this_turn):
    for idx in range(len(matrix)):
        for jdx in range(len(matrix[0])):
            if flashing_this_turn[idx][jdx] :
                matrix[idx][jdx] =0
    return matrix

data = []
with open('Day11_input.txt','r') as f:
     for line in f:
        data.append([int(v) for v in line.replace('\n','')]) 

data =np.array(data)
nr_flash = 0

for time in range(1,500):
    flashes_in_single_time =0
    data +=1
    is_flashing_this_turn = numbers_biggr_9(data)

    while np.any(numbers_biggr_9(data)):
        (is_flashing_this_turn, data, new_flashes)= flash_energize_count(data, is_flashing_this_turn)
        flashes_in_single_time  += new_flashes
    data = reset_counter(data, is_flashing_this_turn)
    nr_flash += flashes_in_single_time
    if flashes_in_single_time == 100:
        print('all jellifishes flashed at time ', time)
        break

print(data)
print(nr_flash)
#%%
