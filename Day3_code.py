
def find_most_common_bin(array):
    size = len(array)
    if(sum(array)>= size/2):
        return 1
    else:
        return 0
    
def find_least_common_bin(array):
    size = len(array)
    if(sum(array)>= size/2):
        return 0
    else:
        return 1    

def bin_array_to_int(array):
    final_value =0
    power_of_two =1
    for idx in range(len(array)):
        final_value += array[len(array)-1-idx]*power_of_two
        power_of_two *=2
    return final_value
    
get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

gamma_rate_ar = [0]*12
epsilon_rate_ar = [0]*12
list_oxy = []
list_CO2 = []
with open('Day3_input.txt') as f:
    for line in f:
        line = line[0:12]
        listed_input = [int(digit) for digit in str(line)]
        list_oxy.append(listed_input)
        list_CO2.append(listed_input)        
        
gamma_rate_ar = [find_most_common_bin([list_oxy[idx_list][idx_bit] for idx_list in range(1000)]) for idx_bit in range(12)]
epsilon_rate_ar = [find_least_common_bin([list_oxy[idx_list][idx_bit] for idx_list in range(1000)]) for idx_bit in range(12)]

gamma_rate =bin_array_to_int(gamma_rate_ar)
epsilon_rate =bin_array_to_int(epsilon_rate_ar)
   
print(gamma_rate*epsilon_rate)


for idx_bit_oxy in range(12):
    most_com_bit =  find_most_common_bin([list_oxy[idx_list][idx_bit_oxy] for idx_list in range(len(list_oxy))])
    list_oxy_temp = list(filter(lambda x : x[idx_bit_oxy] != most_com_bit, list_oxy))
    list_oxy = list_oxy_temp
    if len(list_oxy)==1:
        break
print(list_oxy)
oxy_rate = bin_array_to_int(list_oxy[0])
print(oxy_rate)
        
for idx_bit_CO2 in range(12):
    least_com_bit =  find_least_common_bin([list_CO2[idx_list][idx_bit_CO2] for idx_list in range(len(list_CO2))])
    list_CO2_temp = list(filter(lambda x : x[idx_bit_CO2] != least_com_bit, list_CO2))
    list_CO2 = list_CO2_temp
    if len(list_CO2)==1:
        break
print(list_CO2)
CO2_rate = bin_array_to_int(list_CO2[0])
print(CO2_rate)

print(oxy_rate*CO2_rate)