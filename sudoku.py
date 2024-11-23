import pygame, sys
from Frontend.board import *
from Backend.sudoku_generator import *

def game_buttons(screen, reset, restart, exit):
    reset.button_render(screen, (170, 665))
    restart.button_render(screen, (315, 665))
    exit.button_render(screen, (460, 665))

def difficulty_buttons(screen, easy, med, hard):
    easy.button_render(screen, (170, 500))
    med.button_render(screen, (315, 500))
    hard.button_render(screen, (460, 500))

def draw_board(sudoku, screen):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                continue
            else:
                text_render(str(sudoku[i][j]), 30, 75, ((i * 70) + 35, (j * 70) + 35), screen )

def main():
    pygame.init()
    screen = pygame.display.set_mode((630, 700))
    pygame.display.set_caption('Sudoku')
    screen.fill("white")

    board = Board(3, 3, screen, 0)

    easy_but = Display("./Frontend/easy_button.png", 200, 150)
    med_but = Display("./Frontend/medium_button.png", 200, 150)
    hard_but = Display("./Frontend/hard_button.png", 200, 150)

    reset_but = Display("./Frontend/reset_button.png", 200, 150)
    restart_but = Display("./Frontend/restart_button.png", 200, 150)
    exit_but = Display("./Frontend/exit_button.png", 200, 150)

    draw_welcome(screen)
    difficulty_buttons(screen, easy_but, med_but, hard_but)
    pygame.display.update()


    game_in_progress = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_in_progress:
                x,y = event.pos
                mouse_pos = x,y
                print(x, y)
                if (easy_but.rect.left <= mouse_pos[0] <= easy_but.rect.right
                        and easy_but.rect.top <= mouse_pos[1] <= easy_but.rect.bottom):
                    empty_cells = 30
                    sudoku, solution = generate_sudoku(9, empty_cells)
                    game_in_progress = True
                    screen.fill("light pink")
                    board.draw()
                    game_buttons(screen, reset_but, restart_but, exit_but)

                elif(med_but.rect.left <= mouse_pos[0] <= med_but.rect.right
                        and med_but.rect.top <= mouse_pos[1] <= med_but.rect.bottom):
                    empty_cells = 40
                    sudoku, solution = generate_sudoku(9, empty_cells)
                    game_in_progress = True
                    screen.fill("light pink")
                    board.draw()
                    game_buttons(screen, reset_but, restart_but, exit_but)

                elif(hard_but.rect.left <= mouse_pos[0] <= hard_but.rect.right
                        and hard_but.rect.top <= mouse_pos[1] <= hard_but.rect.bottom):
                    empty_cells = 50
                    sudoku, solution = generate_sudoku(9, empty_cells)
                    game_in_progress = True
                    screen.fill("light pink")
                    board.draw()
                    game_buttons(screen, reset_but, restart_but, exit_but)

            if game_in_progress:
                draw_board(sudoku, screen)
                # text_render(9, 30, 75, (35, 35), screen)
                # text_render("8", 30, 75, (105, 35), screen)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print(x, y)
                    row = y // 70
                    col = x // 70
                    cell_pressed = True

                elif event.type == pygame.KEYDOWN and cell_pressed:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        number = event.key - pygame.K_0
                        print(f"Number pressed: {number}")
                        cell_pressed = False
                        if (sudoku[col][row] == 0):
                            screen.fill("light pink")
                            board.draw()
                            game_buttons(screen, reset_but, restart_but, exit_but)
                            text_render(str(number), "blue", 35, ((col * 70) + 35, (row * 70) + 35), screen)
                            enter = True

                if event.type == pygame.KEYDOWN and enter:
                    if event.key == pygame.K_RETURN:
                        sudoku[col][row] = number
                        screen.fill("light pink")
                        board.draw()
                        game_buttons(screen, reset_but, restart_but, exit_but)
                        # temp = sudoku
                        enter = False

if __name__ == "__main__":
    main()


