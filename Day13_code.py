import numpy as np

def superimpose_lines(line1, line2):
    new_line = ['.' for idx in range(len(line1))]
    for idx in range(len(line1)):
        if line1[idx] =='#' or line2[idx] == '#':
            new_line[idx] = '#'
    return new_line

    
# left, right = 1310, 891

sheet= [['.' for idx in range(1310+1)] for jdx in range(891+1)]


with open('Day13_inputA.txt','r') as f:
     for line in f:
         (left, right) = line.replace('\n','').split(',')
         left = int(left)
         right = int(right)
         sheet[right][left] = '#'

instructions = []
with open('Day13_inputB.txt','r') as f:
    for fold in f:
        instruction = fold.split(' ')[2]
        instructions.append( [instruction[0], int(instruction[2:])])
        
sheet = np.array(sheet)
        
for folding in instructions:
    edge = folding[1]
    if folding[0] == 'x':
        first_col =  2*edge - len(sheet[0])  +1
        print( folding, ' ', len(sheet[0]), first_col)
        for idx in range(0, edge):
            sheet[:,first_col +idx] =superimpose_lines(sheet[:,idx], sheet[:,len(sheet[0]) - idx-1])
        sheet = sheet[:, 0:edge]
    if folding[0] == 'y':
        first_row =  2*edge - len(sheet) +1
        print( folding, ' ', len(sheet), first_row)
        for idy in range(0, edge):
            sheet[first_row + idy] =superimpose_lines(sheet[first_row +idy], sheet[ len(sheet) - idy -1])
        sheet = sheet[0:edge]
    #break
    

           

#%%
#print(np.transpose(sheet))
for idx in range(len(sheet)):
    print(''.join(sheet[idx]))
    
#print(np.count_nonzero(sheet =='#'))    
    
#%%
