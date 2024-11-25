import pygame


class Cell:
    def __init__(
        self,
        value,
        row,
        col,
        screen,
    ):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched = value

    def draw(self):
        for i in range(2):
            # Horizontal small lines
            pygame.draw.line(
                self.screen,
                "black",
                ((self.col * 70), ((i * 70) + (self.row * 70))),
                (((self.col * 70) + 70), ((i * 70) + (self.row * 70))),
                1,
            )
            # Vertical small lines
            pygame.draw.line(
                self.screen,
                "black",
                (((i * 70) + (self.col * 70)), (self.row * 70)),
                ((i * 70) + (self.col * 70), ((self.row * 70) + 70)),
                1,
            )

        # Selection detection
        if self.selected:
            pygame.draw.rect(
                self.screen, "red", pygame.Rect(self.col * 70, self.row * 70, 70, 70), 3
            )

        # Sketch values
        if self.value == 0 and self.sketched == 0:
            pass
        else:
            if self.value == 0 and self.sketched != 0:
                # Draw sketched value
                font = pygame.font.Font(None, 48)
                text_surface = font.render(
                    str(self.sketched), True, "white"
                )  # Gray for sketches
                text_rect = text_surface.get_rect(
                    topleft=(
                        (self.col * 70) + 5,
                        (self.row * 70) + 5,
                    )
                )
                self.screen.blit(text_surface, text_rect)
            elif self.value != 0:
                # Draw permanent value
                font = pygame.font.Font(None, 48)
                text_surface = font.render(str(self.value), True, "black")
                text_rect = text_surface.get_rect(
                    center=(
                        (self.col * 70) + 35,
                        (self.row * 70) + 35,
                    )
                )
                self.screen.blit(text_surface, text_rect)
