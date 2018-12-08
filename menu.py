import pygame


class Menu():
    def __init__(self, screen, color, pos, size):
        self.screen = screen
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.children = []

    # def add_menu_button(self, screen, color, pos, size, text=''):
    #     button = MenuButton(screen, color, pos, size, text)
    #     self.children.append(button)

    def draw(self):

        if not self.screen:
            return

        for child in self.children:
            child.draw()

        pygame.draw.rect(self.screen, self.color,
                         (self.x, self.y, self.width, self.height), 0)


class MenuButton(Menu):
    def __init__(self, screen, color, pos, size, text='', highlight_color=None):
        super().__init__(screen, color, pos, size)
        self.text = text
        self.orig_color = color
        self.highlight_color = highlight_color
        pygame.font.init()

    def draw(self):

        self.mouse_over(pygame.mouse.get_pos())

        super().draw()

        if self.text:
            font = pygame.font.SysFont(
                'Verdana, Segoe UI, Arial, Playbill, Bauhaus 93, Showcard Gothic', int(self.height * 0.75))
            text = font.render(self.text, 1, (0, 0, 0))
            self.screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                                    self.y + (self.height/2 - text.get_height()/2)))

    def mouse_over(self, mouse_pos):

        if not pygame.mouse.get_focused():
            self.color = self.orig_color
            return

        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
                self.color = self.highlight_color
                return True
        self.color = self.orig_color
        return False