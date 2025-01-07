import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable)
    AsteroidField.containers = updatable

    asteroidfield = AsteroidField()
    player = Player(x, y)
    running = True
    while running:
        dt = clock.tick(120)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                return

        for obj in updatable:
            obj.update(dt)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
