#%%

def check_if_winning(board):
    for idx in range(5):
        if all(board[:][idx]) or all([board[jdx][idx] for jdx in range(5)]):
            return True
    return False

def mark_number_in_board(number, board, was_nr_called):
    for idx_row in range(5):
        for idx_col in range(5):
            if number == board[idx_row][idx_col]:
                was_nr_called[idx_row][idx_col] = True
 
def compute_sum(boards,was_nr_called):
    flat_win_board =[]
    flat_was_extr = []
    for idx_row in range(5):
        flat_win_board += boards[idx_row]
        flat_was_extr += was_nr_called[idx_row]

    sum_uncalled =0
    for idx in range(25):
        sum_uncalled += flat_win_board[idx] if flat_was_extr[idx]== False  else 0
        
    return sum_uncalled
                
data = []
with open('Day4_input.txt') as f:
    for line in f:
        data.append([v for v in line.split()]) 
        
numbers_called = [int(s) for s in data.pop(0)[0].split(',')] 

boards = []
for idx_board in range(100):
    new_board = [[int(data[idx_row + 6*idx_board][idx_col]) for idx_col in range(5)] for idx_row in range(1,6)]
    boards.append(new_board)

    
was_nr_called = [[[False for i in range(5)] for j in range(5)] for k in range(100)]
won_at_turn = [0 for i in range(100)]
sum_uncalled_at_win = [0 for i in range(100)]
for idx_extr in range(100):
    nr_extracted = numbers_called[idx_extr]
    for idx_board in range(100):
        mark_number_in_board(nr_extracted, boards[idx_board], was_nr_called[idx_board])
        if (check_if_winning(was_nr_called[idx_board])) and won_at_turn[idx_board] ==0:
            won_at_turn[idx_board]= idx_extr
            sum_uncalled_at_win[idx_board] = compute_sum(boards[idx_board],was_nr_called[idx_board])

idx_winning_board = won_at_turn.index(min(won_at_turn))
idx_last_win_board = won_at_turn.index(max(won_at_turn))

flat_win_board =[]
flat_was_extr = []
for idx_row in range(5):
    flat_win_board += boards[idx_winning_board][idx_row]
    flat_was_extr += was_nr_called[idx_winning_board][idx_row]

sum_uncalled =0
for idx in range(25):
    sum_uncalled += flat_win_board[idx] if flat_was_extr[idx]== False  else 0

print(sum_uncalled_at_win[idx_winning_board]*numbers_called[won_at_turn[idx_winning_board]])
print(sum_uncalled_at_win[idx_last_win_board]*numbers_called[won_at_turn[idx_last_win_board]])


#%%


