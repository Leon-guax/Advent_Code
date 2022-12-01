def is_ver(array):
    return array[0] == array[2] 

def is_hor(array):
    return array[1] == array[3] 

def is_diag_up(array):
    return array[0] - array[2] == array[1] - array[3]

data = []
with open('Day5_input.txt') as f:
     for line in f:
        temp_list =line.replace('\n',"").replace('->',',').split(',')
        data.append([int(v) for v in temp_list]) 
    

diagram = [[0 for idx in range(1000)] for jdx in range(1000)]

for data_line in data:
    if is_hor(data_line):
        direction = range(min(data_line[0], data_line[2]), max(data_line[0], data_line[2])+1)
        for idx_path in direction: 
            diagram[idx_path][data_line[1]] +=1
            
    elif is_ver(data_line):
        direction = range(min(data_line[1], data_line[3]), max(data_line[1], data_line[3])+1)
        for idx_path in direction: 
            diagram[data_line[0]][idx_path] +=1
    else:
        direction_x = range(min(data_line[0], data_line[2]), max(data_line[0], data_line[2])+1)
        if is_diag_up(data_line):
            direction_y = range(min(data_line[1], data_line[3]), max(data_line[1], data_line[3])+1)
            for idx_path_x, idx_path_y in zip(direction_x, direction_y): 
                diagram[idx_path_x][idx_path_y] +=1
        else:
            direction_y = range(max(data_line[1], data_line[3]), min(data_line[1], data_line[3])-1,-1)
            for idx_path_x, idx_path_y in zip(direction_x, direction_y): 
                diagram[idx_path_x][idx_path_y] +=1
    
nr_dang_areas =0            
for diagram_row in diagram:
    nr_dang_areas += len(list(filter(lambda x: x>1, diagram_row)))

print(nr_dang_areas)    