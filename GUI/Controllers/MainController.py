import pygame

from ..Models import MainModel
from ..Views import MainView

class MainController:
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.model = MainModel()
        self.view = MainView(self)
        self._display_surf = None
        self._running = True
 
    def init_pygame(self):
        pygame.init()
        # @todo limit the allowed events to improve performance
        # pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
    def on_loop(self):
        pass
        
    def on_render(self):
        pass
    
    def on_cleanup(self):
        pygame.quit()
 
    def run(self):
        if self.init_pygame() == False:
            self._running = False
 
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()