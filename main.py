import pygame
from pygame.base import init
from player import Player
from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateable.update(dt)

        for draws in drawable:
            draws.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1_000


if __name__ == "__main__":
    main()
