import pygame
import settings
import sys


class App():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.running = True
        self.grid = settings.testBoard
        #print(self.grid)
        self.first_call = True

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pass

    def update(self):
        pass

    def draw(self):
        if self.first_call:
            self.first_call = False
            self.window.fill(settings.WHITE)
            self.draw_grid(self.window)
            pygame.display.update()
        pass

    def draw_grid(self, window):
        pygame.draw.rect(window, settings.BLACK, (settings.gridPos[0], settings.gridPos[1], settings.WIDTH - 150,
                                                  settings.HEIGHT - 150), 3)
        for x in range(9):
            thickness = 1
            if x % 3 == 0:
                thickness = 3

            #vertical lines
            pygame.draw.line(window, settings.BLACK,
                             (settings.gridPos[0] + (x * settings.cellSize), settings.gridPos[1]),
                             (settings.gridPos[0] + (x * settings.cellSize), settings.gridPos[1] + 450), thickness)
            #horizontal lines
            pygame.draw.line(window, settings.BLACK,
                             (settings.gridPos[0], settings.gridPos[1] + (x * settings.cellSize)),
                             (settings.gridPos[0] + 450, settings.gridPos[1] + (x * settings.cellSize)), thickness)

