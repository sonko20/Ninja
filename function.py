from data import *


class Knife(pygame.Rect):
    knife_list = list()
    cut = False

    def __init__(self, x=0,y=0, widht=0, height=0, color=colors["WHITE"]):
        super().__init__(x, y, widht, height)
        self.color = color
        self.time_start = pygame.time.get_ticks()
        self.time_die = 200
        self.radius = 10

    def test_aaline(self, window):
        if len(Knife.knife_list) > 1:
            index = 0
            while len(Knife.knife_list) > index + 1:
                pygame.draw.aaline(window, self.color, Knife.knife_list[index].topleft, Knife.knife_list[index + 1].topleft)
                index += 1

    def remove(self):
        if pygame.time.get_ticks() - self.time_start > self.time_die:
            Knife.knife_list.remove(self)

class Bot(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image

class Bomb(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image