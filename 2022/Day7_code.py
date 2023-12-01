

def find_files(files, string):
    subfolder = {}
    for file in files:
        if string in file.key():
           subfolder[file.key()] = file.value()
    return subfolder
    

files = {}



with open('Day7_input.txt') as f:
    f.readline()
    
    #for line in f:
     #   print(line)
      #  break

#%%
