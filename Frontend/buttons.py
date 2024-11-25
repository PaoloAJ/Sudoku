import pygame


class Button:
    def __init__(self, x, y, image, screen):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 150, 40)
        self.image = pygame.transform.scale(image, self.rect.size)

    def draw(self):
        self.screen.blit(self.image, self.rect)
