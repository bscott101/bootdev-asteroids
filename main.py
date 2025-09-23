import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shoot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable, )
    asteroidfield = AsteroidField()
    Shot.containers = (shots, updateable, drawable)
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateable.update(dt)

        for draws in drawable:
            draws.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("GAME OVER!")
                sys.exit()
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.kill()
                    shot.kill()
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1_000


if __name__ == "__main__":
    main()
