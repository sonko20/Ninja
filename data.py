import pygame
import os
import random

pygame.init()

size_window = (1200, 800)

colors = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "RED": (230, 50, 50),
            "BLUE": (0, 50, 200),
            "GREEN":(55, 141, 50),
            "BLUE_DARK":(38, 106, 103)
}
FPS = 120
fruits_list = list()
cross_list = list()
score_list = list()
abs_path = os.path.abspath(__file__ + "/..")




watermelon_image_list =[

    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "1.png")), (85,94)),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "2.png")), (83, 74))
]

bg_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bg.jpg")), size_window)

red_cross_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "red_cross.png")), (50,50))
blue_cross_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "blue_cross.png")), (50,50))


















