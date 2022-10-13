import pygame
from pygame.locals import *

class MainView():
    def __init__(self, controller):
        self.controller = controller

        # @todo fullscreen when on a specific switch is used? --fullscreen
        # flags = pygame.HWSURFACE | pygame.FULLSCREEN | pygame.DOUBLEBUF
        flags = pygame.HWSURFACE | pygame.DOUBLEBUF
        controller._display_surf = pygame.display.set_mode(controller.size, flags)
