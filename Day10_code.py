import numpy as np
import statistics

def read_data(partsis):
    array = np.zeros(4)
    if partsis == ')':
        array [0] -=1
    elif partsis == ']':
        array [1] -=1
    elif partsis == '}':
        array [2] -=1
    elif partsis == '>':
        array [3] -=1
    return  array 


def log_error_reason(partsis):
    if partsis == ')':
        reason_corrupted_lines[0] +=1
    elif partsis == ']':
        reason_corrupted_lines[1] +=1
    elif partsis == '}':
        reason_corrupted_lines[2] +=1
    elif partsis == '>':
        reason_corrupted_lines[3] +=1
        
def is_still_valid(ton_quad_graf_ang):
    return all(ton_quad_graf_ang>=0)
        
def compute_error_pts(reason_corrupted_lines):
    return int(np.dot(reason_corrupted_lines, [3, 57, 1197, 25137]))
        
def flip_parsis(char):
    if char == '(':
        return 1
    elif char == '[':
        return 2
    elif char == '{':
        return 3
    elif char == '<':
        return 4  

def compute_correction_points(array):
    sum =0
    for pts in array:
        sum = sum*5 + pts
    return sum

data = []
reason_corrupted_lines = np.zeros(4)
with open('Day10_input.txt','r') as f:
     for line in f:
        data.append(line.replace('\n',''))

array_correction_pts = []
nrow = 0
nr_corrupted_lines =0
for row in data:
    nrow +=1
    print('row number ',nrow)
    len_row = len(row)
    len_row_temp = len(row)-1
    while len_row >len_row_temp :
        len_row = len(row)
        row = row.replace("()","")
        row = row.replace("[]","")
        row = row.replace("{}","")
        row = row.replace("<>","")
        len_row_temp = len(row)
    print(row)
     
    is_line_corrupted = False
    ton_quad_graf_ang = np.zeros(4)
    for partsis in row:
        ton_quad_graf_ang = ton_quad_graf_ang + read_data(partsis)

        if not is_still_valid(ton_quad_graf_ang):
            print('corrupted row', nrow)
            log_error_reason(partsis)
            is_line_corrupted = True
            nr_corrupted_lines +=1
            break
    correction_needed_pts = []
    if not is_line_corrupted:
        while(len(row))>0 :
            pars =row[-1]
            row = row[:-1]
            correction_needed_pts.append(flip_parsis(pars))
        array_correction_pts.append(compute_correction_points(correction_needed_pts))
    
print(reason_corrupted_lines)
print(compute_error_pts(reason_corrupted_lines)) 

print(statistics.median(array_correction_pts))
#%%
