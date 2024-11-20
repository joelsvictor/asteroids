# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main ():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # gameloop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    af = AsteroidField()

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    p = Player(x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if (a.check_for_collisions(p)):
                print ("Game over!")
                sys.exit(1)
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
