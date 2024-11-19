import sudoku_generator

sudoku = sudoku_generator.generate_sudoku(9, 50)
for i in sudoku:
    print(i)
    print()