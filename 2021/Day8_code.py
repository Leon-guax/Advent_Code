
def are_strings_eq(string1, string2):
    return len(string1) == len(string2) and string1 == string2

def is_string_contained(string1, string2):
    short_str = string1 if len(string1) <= len(string2) else string2
    long_str  = string1 if len(string1)  > len(string2) else string2    
    for char in short_str:
        if not(char in long_str):
            return False
    return True

def chars_contained_in_str2(str1, str2):
    contained = []
    for char in str1:
        if char in str2:
            contained.append(char)
    return contained

def diff_strs(str1, str2):
    output = str1[:]
    for char in str2:
        output = output.replace(char,"")
    return output

def count_1478(line):
    for idx_line in range(len(line)):
        if len(line[idx_line] )== 2:
            total_counter[1] +=1
        elif len(line[idx_line] )== 4:
            total_counter[4] +=1
        elif len(line[idx_line] )== 3:
            total_counter[7] +=1
        elif len(line[idx_line] )== 7:
            total_counter[8] +=1                  

def decode_line_in(line_in):
    dict_bar2letter ={}
    
    dig_len = ([0]*10)[:]
    dict_cyphers = {}
    for idx_string in range(len(line_in)):
            dig_len[idx_string] = len(line_in[idx_string])
    ord_zip_dig_len = sorted(list(zip(line_in, dig_len)),key= lambda x:x[1])   
    
    dict_cyphers[1] = ord_zip_dig_len[0][0]
    dict_cyphers[4] = ord_zip_dig_len[2][0]
    dict_cyphers[7] = ord_zip_dig_len[1][0]
    dict_cyphers[8] = ord_zip_dig_len[9][0]
    
    dict_bar2letter['top']= diff_strs(dict_cyphers[7],  dict_cyphers[1])
    
    for dig in range (3,6):
          if is_string_contained(dict_cyphers[1], ord_zip_dig_len[dig][0]):  
             dict_cyphers[3] = ord_zip_dig_len[dig][0] 
             break
    cenORbot =diff_strs(dict_cyphers[3], dict_cyphers[7])
    
    dict_bar2letter['bot'] = diff_strs(cenORbot, dict_cyphers[4])
    dict_bar2letter['cen'] = diff_strs(cenORbot, dict_bar2letter['bot'])
    dict_bar2letter['tl'] = diff_strs(diff_strs(dict_cyphers[4],dict_cyphers[1]),dict_bar2letter['cen'])
    five_minus_br = (dict_bar2letter['cen'] + dict_bar2letter['bot'] 
                    + dict_bar2letter['top'] + dict_bar2letter['tl'])
    
    for dig in range (3,6): 
        if len(diff_strs(ord_zip_dig_len[dig][0], five_minus_br)) == 1 :
            dict_bar2letter['br'] =diff_strs(ord_zip_dig_len[dig][0], five_minus_br)           
            dict_cyphers[5] = ord_zip_dig_len[dig][0]
            break
    dict_bar2letter['tr'] = diff_strs(dict_cyphers[1], dict_bar2letter['br'])
    
    nine =(dict_bar2letter['cen'] + dict_bar2letter['bot'] + dict_bar2letter['top']
           + dict_bar2letter['tl'] + dict_bar2letter['tr'] + dict_bar2letter['br'])
    
    for dig in range(6,9):
        if is_string_contained(nine, ord_zip_dig_len[dig][0]):
            dict_cyphers[9] = ord_zip_dig_len[dig][0]
            break
    dict_bar2letter['bl'] = diff_strs(dict_cyphers[8], dict_cyphers[9])
    
    dict_cyphers[6] = diff_strs(dict_cyphers[8],  dict_bar2letter['tr'])
    dict_cyphers[0] = diff_strs(dict_cyphers[8],  dict_bar2letter['cen'])
    dict_cyphers[2] = diff_strs(dict_cyphers[8], dict_bar2letter['tl']+ dict_bar2letter['br'])
    
    return (dict_cyphers, dict_bar2letter)
    
    
    


total_sum = 0
total_counter = ([0]*12)[:]
with open('Day8_input.txt','r') as f:
    for line in f:
        line_digits = ''
        line_in = []
        line_out = []
        for digit in line.split('|')[0].split():
            line_in.append(''.join(sorted(digit)))
        for digit in line.split('|')[1].split():
            line_out.append(''.join(sorted(digit))) 

        count_1478(line_out)
                
        
        (decoding, dict_bar2letter) = decode_line_in(line_in)
        
        for idx_line in range(4):
            for digit in decoding:
                    if line_out[idx_line] == decoding[digit]:
                        line_digits+= str(digit)
                        break
        total_sum += int(line_digits)
            
        
print('-'*12)    
print(sum(total_counter))
print(total_sum)
