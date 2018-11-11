import arcade
import random
import math

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_WIDTH // 2


class Vector:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    
class Point:
    def __init__(self, x ,y):
        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)

    def draw(self):
        arcade.draw_point(self.pos.x, self.pos.y, arcade.color.RED, 10)

    def update(self):
        self.pos.add(self.vel)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Appication")
        self.point = Point(200, 200)

    def on_draw(self):
        arcade.start_render()

        self.point.draw()

    def update(self, delta_time):
        self.point.update()

        if self.point.pos.x > SCREEN_WIDTH:
            self.point.vel = Vector(-5, 0)
        if self.point.pos.x < 0:
            self.point.vel = Vector(5, 0)

    def on_key_release(self, key, modifiers):
        if self.point.vel.x == 0:
            self.point.vel = Vector(5, 2)
        elif self.point.vel.x > 0:
            self.point.vel = Vector(-5, 0)
        else:
            self.point.vel = Vector(5, 0)


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()