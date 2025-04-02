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
}
FPS = 120

abs_path = os.path.abspath(__file__ + "/..")

