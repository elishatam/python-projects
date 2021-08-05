import sys
sys.path.insert(0, '../')  #Look 1 directory higher to find these files
import pygame
from player import HumanPlayer
from screen import Screen
from game import Game, HardGame
from main import play_game


if __name__ == "__main__":
    pygame.init()

    screen = Screen()
    player = HumanPlayer(screen.width/2, screen.height-100)
    game = HardGame()

    play_game(screen, player, game)