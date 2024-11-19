import random

test_board = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def fill_box(row_start, col_start):
    unused_in_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(row_start ,row_start + 3):
        for j in range(col_start, col_start + 3):
            while True:
                random_number = random.randint(1,9)
                if random_number in unused_in_box:
                    test_board[i][j] = random_number
                    unused_in_box.remove(random_number)
                    break
                else:
                    continue

def fill_diagonal():
        row_start = 0
        col_start = 0
        for i in range(3):
            fill_box(row_start, col_start)
            row_start += 3
            col_start += 3

def remove_cells():
        for i in range(4):
            while True:
                random_row = random.randint(0, 8)
                random_col = random.randint(0, 8)
                print(random_row, random_col)
                if test_board[random_row][random_col] != 0:
                    print("True")
                    test_board[random_row][random_col] = 0
                    break
                else:
                    print("False")
                    continue



fill_diagonal()
for i in test_board:
    print(i)
    print()
remove_cells()
print()
for i in test_board:
    print(i)
    print()

# for i in test_board:
#     print(i)
#     print()
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