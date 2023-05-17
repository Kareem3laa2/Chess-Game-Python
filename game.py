import pygame

from const import *



class Game:
    def __init__(self) -> None:
        pass

    #show methods

    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234,234,200) #Light green
                else:
                    color = (119,154,88)  #Dark green
                rect = (col * SQIZE, row * SQIZE, SQIZE,SQIZE)

                pygame.draw.rect(surface,color,rect)