import numpy as np

def supl_norm(l1_dist):
    return l1_dist*(l1_dist+1)/2

with open('Day7_input.txt','r') as f:
     data = [int(element) for element in f.read().split(',')] 
     
     
data_median = round(np.median(data))

fuel_cost = sum([abs(data[idx]-data_median) for idx in range(len(data))])

print(fuel_cost)

data_avg = int(float(sum(data))/len(data)) #not sure why int() and not round()

fuel_cost_supl = int(sum([supl_norm(abs(data[idx]-data_avg)) for idx in range(len(data))]))
print(fuel_cost_supl)

