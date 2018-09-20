import arcade
import random
import math
# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
FULL_VISIBLE = 255

# (x - x1) * (y2 - y1) - (x2 - x1) * (y - y1) = 0
def check_point(x1, y1, x2, y2, x, y):
    val = (x - x1) * (y2 - y1) - (x2 - x1) * (y - y1)
    return val >= -150 and val <= 150 and (x > x1 and x < x2 or x > x2 and x < x1)
    # return val == 0

class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0
        self.visible = False

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

    def update(self):
        if self.visible:
            self.color[3] = self.color[3] - 2

        if self.color[3] <= 0:
            self.visible = False
            self.color[3] = FULL_VISIBLE

class Sweep:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sweep_length = 250
        self.angle = 0.0
        self.angle_per_frame = 0.01

    def draw(self):
        # Draw the outline of the radar
        arcade.draw_circle_outline(CENTER_X, CENTER_Y, self.sweep_length,
                                   arcade.color.DARK_GREEN, 10)

        # Draw the line of the radar.
        arcade.draw_line(CENTER_X, CENTER_Y, self.x, self.y, arcade.color.OLIVE, 4)

    def update(self):
        self.angle += self.angle_per_frame

        # Calculate the end point of our radar sweep. Using math.
        self.x = self.sweep_length * math.sin(self.angle) + CENTER_X
        self.y = self.sweep_length * math.cos(self.angle) + CENTER_Y


def make_ball(x, y):
    """
    Function to make a new, random ball.
    """
    ball = Ball()

    # Size of the ball
    ball.size = random.randrange(5, 10)

    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = int(x)
    ball.y = int(y)

    # Color
    ball.color = [random.randrange(256), random.randrange(256), random.randrange(256), FULL_VISIBLE]

    return ball


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Bouncing Balls Demo")
        self.ball_list = []
        self.sweep = Sweep()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        output = "Balls: {}".format(len(self.ball_list))
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        self.sweep.draw()

        for ball in self.ball_list:
            if ball.visible:
                ball.draw()

    def update(self, delta_time):
        self.sweep.update()

        for ball in self.ball_list:
            if not ball.visible and check_point(CENTER_X, CENTER_Y, self.sweep.x, self.sweep.y, ball.x, ball.y):
                ball.visible = True

            ball.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """
        Called whenever the mouse button is clicked.
        """
        print(x, y)


    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        ball = make_ball(x, y)
        self.ball_list.append(ball)



def main():
    game = MyGame()
    game.set_update_rate(1 / 60)
    arcade.run()


if __name__ == "__main__":
    main()