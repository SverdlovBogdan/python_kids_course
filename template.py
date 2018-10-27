import arcade
import random
import math

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_WIDTH // 2

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Appication")

    def on_draw(self):
        arcade.start_render()

    def update(self, delta_time):
        pass

    def on_key_release(self, key, modifiers):
        pass


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()