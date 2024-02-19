import pygame
class Text:
    def __init__(self, text, text_colour, px, py, font_type=None, font_size=74):
        self.text = str(text)
        font = pygame.font.SysFont(font_type, font_size)
        self.image = font.render(self.text, True, text_colour)
        self.text_color = text_colour
        self.font = pygame.font.SysFont(font_type, font_size)
        self.update()
        self.rect = self.image.get_rect()
        self.rect.center = px, py

    def draw(self, surface):
        self.update()
        surface.blit(self.image, self.rect)

    def update(self):
        self.image = self.font.render(self.text, True, self.text_color)