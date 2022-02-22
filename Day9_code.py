import numpy as np
from skimage.measure import label

data = []
is_local_min = [[True for idx in range(100)] for jdx in range(100)]
risk_level_sum = 0

def is_smaller_than_dir(position, direction):
    return (data[position[0]][position[1]] < data[position[0]+direction[0]][position[1]+direction[1]] )


with open('Day9_input.txt','r') as f:
    print(f)
    for line in f:
        data.append([int(digit) for digit in line.replace('\n','')])
             
for idx_row in range(100):
    for idx_col in range(100):
        
        if idx_col >0 :
            is_local_min[idx_row][idx_col] = is_smaller_than_dir([idx_row, idx_col], [0,-1])
        if is_local_min[idx_row][idx_col] and idx_col <99 :
            is_local_min[idx_row][idx_col] = is_smaller_than_dir([idx_row, idx_col], [0, 1])            
        if is_local_min[idx_row][idx_col] and  idx_row >0 :
            is_local_min[idx_row][idx_col] = is_smaller_than_dir([idx_row, idx_col], [-1,0])   
        if is_local_min[idx_row][idx_col] and idx_row <99 :
            is_local_min[idx_row][idx_col] = is_smaller_than_dir([idx_row, idx_col], [1, 0])
        
        if is_local_min[idx_row][idx_col]:
            risk_level_sum += data[idx_row][idx_col] +1
            
            
print(risk_level_sum)

#%%
image_holes = np.ndarray([100, 100], dtype=int, buffer=None, offset=0, strides=None, order=None)
for idx_row in range(100):
    for jdx_col in range(100):
        image_holes[idx_row][jdx_col] = 1 if data[idx_row][jdx_col] == 9 else 0


