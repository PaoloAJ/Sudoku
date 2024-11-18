import random

test_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for i in range(len(test_board)):
    col = int(5)
    print(test_board[i][col])

def fill_box(row_start, col_start):
    unused_in_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(row_start - 1 ,row_start + 2):
        for j in range(col_start -1, col_start + 2):
            while True:
                random_number = random.randint(1,9)
                if random_number in unused_in_box:
                    test_board[i][j] = random_number
                    unused_in_box.remove(random_number)
                    break
                else:
                    continue

def fill_diagonal():
        row_start = 1
        col_start = 1
        for i in range(3):
            fill_box(row_start, col_start)
            row_start += 3
            col_start += 3


fill_diagonal()

for i in test_board:
    print(i)
    print()
# Valid in box
# for i in range(row_start - 1 ,row_start + 2):
#     for j in range(col_start -1, col_start + 2):
#         print(test_board[i][j], end="")
#     print()

# for i in test_board:
#     print(i[0])

# board = []
# class Test:
#     def __init__(self, board):
#         self.board = board
    
# test = Test(test_board)

# test_nums = [1, 2, 3, 4]
# test_nums.remove(5)
# print(test_nums)
# random_number = random.randint(1,9)
# print(random_number)