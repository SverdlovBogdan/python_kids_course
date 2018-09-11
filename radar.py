import arcade
import random
import math
# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
RADIANS_PER_FRAME = 0.01
SWEEP_LENGTH = 250

ANGLE = 0.0

# (x - x1) * (y2 - y1) - (x2 - x1) * (y - y1) = 0

def check_point(x1, y1, x2, y2, x, y):
    val = (x - x1) * (y2 - y1) - (x2 - x1) * (y - y1)
    return val >= -100 and val <= 100 and (x > x1 and x < x2 or x > x2 and x < x1)
    # return val == 0

class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0
        self.draw = False


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
    ball.color = (random.randrange(256), random.randrange(256), random.randrange(256))

    return ball


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Bouncing Balls Demo")
        self.ball_list = []

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()


        # Put the text on the screen.
        output = "Balls: {}".format(len(self.ball_list))
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        global ANGLE
        ANGLE += RADIANS_PER_FRAME

        # Calculate the end point of our radar sweep. Using math.
        x = SWEEP_LENGTH * math.sin(ANGLE) + CENTER_X
        y = SWEEP_LENGTH * math.cos(ANGLE) + CENTER_Y
        # print(int(x), int(y))

        # Draw the radar line
        arcade.draw_line(CENTER_X, CENTER_Y, x, y, arcade.color.OLIVE, 4)

        # Draw the outline of the radar
        arcade.draw_circle_outline(CENTER_X, CENTER_Y, SWEEP_LENGTH,
                                arcade.color.DARK_GREEN, 10)

        for ball in self.ball_list:
            if check_point(CENTER_X, CENTER_Y, int(x), int(y), ball.x, ball.y):
                arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)
                ball.draw = True
            elif ball.draw:
                arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)

    def update(self, delta_time):
        """ Movement and game logic """
        pass

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
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()