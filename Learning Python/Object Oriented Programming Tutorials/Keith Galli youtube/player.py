import pygame
#https://www.youtube.com/watch?v=731LoaZCUjo&list=PLFCB5Dp81iNVoB_eWmDB1nEusSCurrsac&index=10
from color import Color


class Player:
    def __init__(self, x, y, size, color=Color.RED):
        self.x = x  #player position
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def detect_collision(self, other):
        # X needs to overlap
        if(other.x >= self.x and other.x < (self.x + self.size)) or (self.x >= other.x and self.x < (other.x + other.size)):
            # Y also needs to overlap
            if (other.y >= self.y and other.y < (self.y + self.size)) or (self.y >= other.y and self.y < (other.y + self.size)):
                return True
        return False


#More restrictive version of Player class
class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color=Color.BLUE)

class LargeEnemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=100, color=Color.BLUE)

class HumanPlayer(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color=Color.RED)

class KeithEnemy(Player):
    img = pygame.image.load("../assets/image.JPG")
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color=Color.RED)

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        scaled_img = pygame.transform.scale(self.img, rect.size)
        scaled_img = scaled_img.convert()
        screen.blit(scaled_img, rect)
