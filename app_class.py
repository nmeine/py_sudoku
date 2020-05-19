import pygame
import settings
import sys
import math


class App():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.running = True
        self.grid = settings.testBoard
        self.first_call = True
        self.selected = None
        self.mouse_position = None

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if(self.mouse_on_grid()):
                    self.selected = self.get_mouse_index()
                    print(self.selected)
                else:
                    self.selected = None
        pass

    def update(self):
        self.mouse_position = pygame.mouse.get_pos()

    def draw(self):
        if self.first_call:
            self.first_call = False
            self.window.fill(settings.WHITE)
            self.draw_grid(self.window)
            pygame.display.update()
        elif self.selected:
            self.draw_selection(self.window, self.selected)
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

    def mouse_on_grid(self):
        if settings.XMIN <= pygame.mouse.get_pos()[0] <= settings.XMAX and settings.YMIN <= pygame.mouse.get_pos()[1] <= settings.YMAX:
            return True
        else:
            return False

    def get_mouse_index(self):
        index = []
        x_pos = pygame.mouse.get_pos()[0] - settings.XMIN
        x_index = math.floor(x_pos / settings.cellSize)
        index.append(x_index)
        y_pos = pygame.mouse.get_pos()[1] - settings.YMIN
        y_index = math.floor(y_pos / settings.cellSize)
        index.append(y_index)
        return index

    def draw_selection(self, window, pos):
        pass

