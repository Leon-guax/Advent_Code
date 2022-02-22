import numpy as np

def sort_dict(dic):
    dict_sort={}
    for i in sorted(dic):
       dict_sort[i]=dic[i]
    return dict_sort

def apply_rule(lef_char, rig_char):
    new_char = ''
    combo = lef_char+ rig_char

    if combo in rules:
        new_char = rules[combo]
    return new_char

def clean_empty_spaces(array):
    return [letter for letter in array if letter]

def most_common(lst):
    return max(set(lst), key=lst.count)

def least_common(lst):
    return min(set(lst), key=lst.count)

rules ={}
polymer = list('NCOPHKVONVPNSKSHBNPF')
polymer_couples = [polymer[idx] +polymer[idx+1] for idx in range(len(polymer)-1)]
with open('Day14_input.txt','r') as f:
     for line in f:
          rules[line.split(' -> ')[0]] =line.split(' -> ')[1].replace('\n','')

rules = sort_dict(rules)

letters = sorted(set(''.join(sorted(set(rules)))))

letters_dict ={}
for idx in range(10):
    letters_dict[letters[idx]] = idx   
letters_mat = [['' for idx in range(10)] for jdx in range(10)]

for rule in rules:
    letters_mat[letters_dict[rule[0]]][letters_dict[rule[1]]] = rules[rule]

couples_mat = np.zeros([100, 100])
couples_dict ={}
for idx, rule in zip(range(100), rules):
    couples_dict[rule] = idx   


    
for rule in rules:
    new_char = rules[rule]
    lef_char = rule[0]
    rig_char = rule[1]
    couples_mat[couples_dict[rule]][couples_dict[lef_char+new_char]] = 1
    couples_mat[couples_dict[rule]][couples_dict[new_char+rig_char]] = 1

couples_mat = np.int64(couples_mat)
# result = couples_mat
# for iterations in range(40):
#     result = np.dot(result, couples_mat)
#     print(iterations, ')  ',result.max(), result.min(), result.sum())


starting_couples = np.zeros(100)
for couple in polymer_couples:
    starting_couples[couples_dict[couple]] =1

new_couples = starting_couples[:]   

for iterations in range(40):
    
    new_couples = couples_mat.dot(new_couples)
    #print(new_couples, '\n')
    # new_pol = [polymer[int(idx/2)] if idx%2 ==0 else '' for idx in range(2*len(polymer)-1)]                
    # for jdx in range(len(polymer)-1):
    #     new_pol[2*jdx +1] = apply_rule(new_pol[2*jdx],new_pol[2*jdx +2])   
    # polymer = clean_empty_spaces(new_pol)
    
most_common_letter = most_common(polymer)
least_common_letter = least_common(polymer)

diff_max_min = polymer.count(most_common_letter) - polymer.count(least_common_letter)


#%%


#%%
