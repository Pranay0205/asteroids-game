from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        a1_velocity = self.velocity.rotate(random_angle) * 1.2
        a2_velocity = self.velocity.rotate(random_angle * -1) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position
        asteroid_1 = Asteroid(x, y, new_radius)
        asteroid_2 = Asteroid(x, y, new_radius)
        asteroid_1.velocity = a1_velocity
        asteroid_2.velocity = a2_velocity
