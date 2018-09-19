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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Math Rose")
        self.k = 7
        self.n = 1
        self.d = 1

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        points_list = []

        angle = 0.0
        step = 0.01
        end = 20 * math.pi
        self.k = self.n / self.d

        while angle < end:
            radius = 200
            x = radius * math.cos(angle) * math.cos(self.k * angle) + CENTER_X
            y = radius * math.sin(angle) * math.cos(self.k * angle) + CENTER_Y
            points_list.append((x, y))
            # arcade.draw_point(x, y, arcade.color.YELLOW, 1)
            angle += step

        # arcade.draw_points(points_list, arcade.color.YELLOW, 1)
        arcade.draw_commands.draw_line_strip(points_list, arcade.color.TROPICAL_RAIN_FOREST, 1)

    def update(self, delta_time):
        pass

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP:
            self.n = self.n + 1
        elif key == arcade.key.DOWN:
            self.n = self.n - 1
        elif key == arcade.key.W:
            self.d = self.d + 1
        elif key == arcade.key.S:
            self.d = self.d - 1

        print(self.n, self.d)


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()