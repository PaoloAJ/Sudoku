import sudoku_generator

sudoku = sudoku_generator.generate_sudoku(9, 50) #50 is the number of cells removed, so let's try 0 
for i in sudoku:
    print(i)
    print() #I lowkey don't have myt headpgones on but just pull the new branch and test it