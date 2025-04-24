from data import *


class Knife(pygame.Rect):
    knife_cords_list = list()
    cut = False

    def __init__(self, x=0,y=0, widht=0, height=0, color=colors["WHITE"]):
        super().__init__(x, y, widht, height)
        self.color = color
        self.time_start = pygame.time.get_ticks()
        self.time_die = 200
        self.radius = 10

    def line(self, window):
        if len(Knife.knife_cords_list) > 1:
            index = len(Knife.knife_cords_list) - 1
            length = index
            widht = 1
            while index > 0:

                if index == length:
                    widht == 1
                elif index == length - 1:
                    widht = 7
                elif index == length - 2:
                    widht = 15
                elif index < length - length / 1.25:
                    widht = 1
                elif index < length - length / 1.5:
                    widht = 3
                elif index < length - length / 2:
                    widht = 5
                elif index < length - length / 4:
                    widht = 7
                elif index < length - length / 6:
                    widht = 9
                elif index < length - length / 8:
                    widht = 11
                elif index < length - length / 10:
                    widht = 13   
                if index == 1:
                    widht == 1
                pygame.draw.line(window, self.color, Knife.knife_cords_list[index].topleft, Knife.knife_cords_list[index - 1].topleft, widht)

                index -= 1

    def remove(self):
        if pygame.time.get_ticks() - self.time_start > self.time_die:
            Knife.knife_cords_list.remove(self)

class Object():
    def __init__(self, x, y, width, height, image_list, half = False, move_x = -1, power_throw = -1):
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_now = self.image
        self.half = half
        self.rect = self.image_now.get_rect(topleft=(x, y))
        self.power_throw = power_throw
        self.gravity_power = 2
        self.rotate = 0.4
        self.angle = 0
        self.move_x = move_x
        if x + 225 * self.move_x > size_window[0] and not self.half:
            self.move_x *= -1

        self.test = 0
        self.test_time_on_air = 225    

    def collide(self, knife_list):
        for knife in knife_list:
            if not self.half and self.rect.collidepoint(knife.x, knife.y):
                return True
        return False

    def move(self):
        if self.rect.y < size_window[1]:
            self.test += 1

        self.rect.y += self.gravity_power
        self.rect.x += self.move_x
        if self.power_throw > 0:
            self.power_throw -= 0.2
            self.rect.y -= self.power_throw
        else:
            self.gravity_power += 0.05

        self.image_now = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image_now.get_rect(center=(self.rect.centerx, self.rect.centery))
        self.angle += self.rotate

    def remove(self):
        if self.rect.y > size_window[1] + self.rect.height + 50:
            return True
        return False    

class Fruit(Object):

    lost_fruit = 0

    def __init__(self, x, y, width, height, image_list, half=False, move_x=-1, power_throw=-1):
        super().__init__(x, y, width, height, image_list, half, move_x, power_throw)

    def collide(self, knife_list):
        if super().collide(knife_list):
            self.image = self.image_list[1]
            self.half = True
            return True
        return False

    def remove(self):
        if super().remove():
            if not self.half:
                CrossLife.hp -= 1
                cross_list[CrossLife.hp].change_image()
            fruits_list.remove(self)    

class  CrossLife():

    hp = 3

    def __init__(self, x, y, cross_list):
        self.x = x
        self.y = y
        self.cross_list = cross_list
        self.image = self.cross_list[0]

    def change_image(self):
        self.image = self.cross_list[1]    
    



