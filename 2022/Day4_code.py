from interval import interval


included_sets =0
overlap_sets =0
with open('Day4_input.txt') as f:
    for line in f:
        line = line.replace("-",",").split(",")
        elf1 = interval[line[0], line[1]]
        elf2 = interval[line[2], line[3]]
        if (elf1 in elf2) or (elf2 in elf1):
           included_sets +=1
        
        if len(elf1 & elf2):
            overlap_sets +=1
        #if (line[0]==line[2]) or (line[0]>line[2] and line[1]<=line[3]) or (line[0]<line[2] and line[1]>=line[3]):
        #    included_sets+=1
            
            
            
print(included_sets, overlap_sets)



#%%
