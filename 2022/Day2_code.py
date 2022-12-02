RPS_mat = [[4,8,3],[1, 5, 9],[7, 2, 6]]

RPS_mat_part_2 = [[3,4,8], [1,5,9],[2,6,7]]

ad_dic = {'A':0,
          'B':1,
          'C':2 }
my_dic = {'X':0,
          'Y':1,
          'Z':2 }

tot_points =0
tot_points_part_2 =0
with open('Day2_input.txt') as f:
     for line in f:
         tot_points += RPS_mat[ad_dic[line[0]]][my_dic[line[2]]]
         tot_points_part_2 += RPS_mat_part_2[ad_dic[line[0]]][my_dic[line[2]]]        
         

print(tot_points) 
print(tot_points_part_2)        
         



example = ['A Y',
           'B X',
           'C Z']

for line in example:
    print(RPS_mat[ad_dic[line[0]]][my_dic[line[2]]])