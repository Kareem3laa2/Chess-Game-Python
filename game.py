import pygame
from board import  Board
from const import *



class Game:
    def __init__(self):
        self.board = Board()

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


    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * SQIZE + SQIZE // 2 , row * SQIZE + SQIZE // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img,piece.texture_rect)
                    