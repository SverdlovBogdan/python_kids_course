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

class Particale:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.vel_y = 0.0
        self.acc_x = 0.0
        self.acc_y = 0.0

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

    def draw(self):
        arcade.draw_point(self.x, self.y, arcade.color.RED_PURPLE, 5)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Fireworks")

        self.fireworks = Particale(CENTER_X, 0)
        self.fireworks.vel_y = 5

    def on_draw(self):
        arcade.start_render()

        self.fireworks.draw()

    def update(self, delta_time):
        self.fireworks.apply_force(0, GRAVITY)
        self.fireworks.update()

    def on_key_release(self, key, modifiers):
        pass


def main():
    game = MyGame()
    game.set_update_rate(1 / 60)
    arcade.run()


if __name__ == "__main__":
    main()