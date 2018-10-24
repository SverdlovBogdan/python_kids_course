import arcade
import random
import math
import copy

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_WIDTH // 2

SQUARE_SIZE = 5
HALF_SQUARE_WIDTH = SQUARE_SIZE // 2
HALF_SQUARE_HEIGHT = SQUARE_SIZE // 2

COLS = int(SCREEN_WIDTH // SQUARE_SIZE)
ROWS = int(SCREEN_HEIGHT // SQUARE_SIZE)
print(COLS, ROWS)

# COLS = 20
# ROWS = 20

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Appication")

        self.buffer_1 = [[0 for x in range(COLS)] for y in range(ROWS)]
        self.buffer_2 = [[0 for x in range(COLS)] for y in range(ROWS)]
        self.point_list = []
        self.color_list = []

        self.draw_buffer = arcade.ShapeElementList()

    def setup(self):
        self.draw_buffer = arcade.ShapeElementList()

    def on_draw(self):
        arcade.start_render()

        self.draw_buffer.draw()

    def update(self, delta_time):
        color_list = []
        point_list = []

        damping = 0.9
        for y in range(1, ROWS - 1):
            for x in range(1, COLS - 1):
                self.buffer_2[y][x] = (self.buffer_1[y][x - 1] + self.buffer_1[y][x + 1] + self.buffer_1[y + 1][x] + self.buffer_1[y - 1][x]) / 2 - self.buffer_2[y][x]
                self.buffer_2[y][x] = self.buffer_2[y][x] * damping

                if self.buffer_2[y][x] <= 0.5:
                    continue

                for i in range(4):
                    color_list.append((self.buffer_2[y][x] * 255, self.buffer_2[y][x] * 255, self.buffer_2[y][x] * 255))

                new_x = SQUARE_SIZE * x
                new_y = SQUARE_SIZE * y

                top_left = (new_x - HALF_SQUARE_WIDTH, new_y + HALF_SQUARE_HEIGHT)
                top_right = (new_x + HALF_SQUARE_WIDTH, new_y + HALF_SQUARE_HEIGHT)
                bottom_right = (new_x + HALF_SQUARE_WIDTH, new_y - HALF_SQUARE_HEIGHT)
                bottom_left = (new_x - HALF_SQUARE_WIDTH, new_y - HALF_SQUARE_HEIGHT)

                # Add the points to the points list.
                # ORDER MATTERS!
                # Rotate around the rectangle, don't append points caty-corner

                point_list.append(top_left)
                point_list.append(top_right)
                point_list.append(bottom_right)
                point_list.append(bottom_left)

        shape = arcade.create_rectangles_filled_with_colors(point_list, color_list)
        self.draw_buffer = arcade.ShapeElementList()
        self.draw_buffer.append(shape)

        self.buffer_1, self.buffer_2 = self.buffer_2, self.buffer_1


    def on_key_release(self, key, modifiers):
        pass

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        self.buffer_1[y // SQUARE_SIZE][x // SQUARE_SIZE] = 255

    # def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    #     """ Override this function to add mouse functionality. """
    #     self.buffer_1[y // SQUARE_SIZE][x // SQUARE_SIZE] = 255


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()