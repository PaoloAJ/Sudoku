import pygame, sys
from Frontend.board import *

def game_buttons(screen, reset, restart, exit):
    reset.button_render(screen, (170, 665))
    restart.button_render(screen, (315, 665))
    exit.button_render(screen, (460, 665))

def difficulty_buttons(screen, easy, med, hard):
    easy.button_render(screen, (170, 500))
    med.button_render(screen, (315, 500))
    hard.button_render(screen, (460, 500))

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
                    game_in_progress = True

                elif(med_but.rect.left <= mouse_pos[0] <= med_but.rect.right
                        and med_but.rect.top <= mouse_pos[1] <= med_but.rect.bottom):
                    empty_cells = 40
                    game_in_progress = True

                elif(hard_but.rect.left <= mouse_pos[0] <= hard_but.rect.right
                        and hard_but.rect.top <= mouse_pos[1] <= hard_but.rect.bottom):
                    empty_cells = 30
                    game_in_progress = True

                if game_in_progress:
                    screen.fill("light pink")
                    board.draw()
                    game_buttons(screen, reset_but, restart_but, exit_but)
                    # text_render(9, 30, 75, (35, 35), screen)
                    # text_render("8", 30, 75, (105, 35), screen)
                    pygame.display.update()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(x, y)
                row = y // 70
                col = x // 70
                print(row, col)


if __name__ == "__main__":
    main()

