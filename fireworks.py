import arcade
import random
import math

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_WIDTH // 2

GRAVITY = -0.05
PARTICLE_VEL_Y = 5.0

PARTICLE_VEL_Y_RANGE = [5.0, 6.0]

# 1 step create particle class.
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.acc_x = 0.0
        self.acc_y = 0.0
        self.size = 5
        self.visibility = 255
        self.color = [228, 0, 120, self.visibility]

    def apply_force(self, x, y):
        self.acc_x += x
        self.acc_y += y

    def update(self):
        self.vel_x += self.acc_x
        self.vel_y += self.acc_y

        self.x += self.vel_x
        self.y += self.vel_y

        self.acc_x = 0
        self.acc_y = 0

        if self.color[3] - 2 > 0:
            self.color[3] = self.color[3] - 2

    def draw(self):
        arcade.draw_point(self.x, self.y, self.color, self.size)

class Fireworks:
    def __init__(self):
        self.main_particles = []
        self.small_particles = []

    def update(self):
        alive_main_particles = []
        explosed_particles = []
        alive_small_particles = []

        for i in self.main_particles:
            i.apply_force(0, GRAVITY)
            i.update()

            if i.vel_y > 0:
                alive_main_particles.append(i)
            else:
                explosed_particles.append(i)

        for i in explosed_particles:
            for k in range(0, 50):
                particle = Particle(i.x, i.y)
                particle.vel_x = random.uniform(-1, 1)
                particle.vel_y = random.uniform(-1, 1)

                particle.vel_x *= random.uniform(1, 1.5)
                particle.vel_y *= random.uniform(1.5, 2.0)

                particle.size = 2
                particle.color = [random.randrange(256), random.randrange(256), random.randrange(256), particle.visibility]
                self.small_particles.append(particle)

        for i in self.small_particles:
            i.apply_force(0, GRAVITY)
            i.update()

            if i.y >= 0:
                alive_small_particles.append(i)

        self.main_particles = alive_main_particles
        self.small_particles = alive_small_particles

    def draw(self):
        for i in self.main_particles:
            i.draw()

        for i in self.small_particles:
            i.draw()

    def add_particle(self):
        particle = Particle(random.randint(0, SCREEN_WIDTH), 0)
        particle.vel_y = random.uniform(PARTICLE_VEL_Y_RANGE[0], PARTICLE_VEL_Y_RANGE[1])
        self.main_particles.append(particle)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Fireworks")

        self.fireworks = Fireworks()

    def on_draw(self):
        arcade.start_render()

        self.fireworks.draw()

    def update(self, delta_time):
        if random.randint(0, 100) < 10:
            self.fireworks.add_particle()

        self.fireworks.update()

    def on_key_release(self, key, modifiers):
        pass


def main():
    game = MyGame()
    game.set_update_rate(1 / 60)

    arcade.run()


if __name__ == "__main__":
    main()