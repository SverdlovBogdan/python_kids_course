"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

class Paddle:
    def __init__(self, is_left):
        self.h = 60
        self.w = 10

        if is_left:
            self.pos = Vector(self.w / 2, SCREEN_HEIGHT / 2)
        else:
            self.pos = Vector(SCREEN_WIDTH - self.w / 2, SCREEN_HEIGHT / 2)
        
        self.vel = Vector(0, 0)

    def draw(self):
        arcade.draw_rectangle_filled(self.pos.x, self.pos.y, self.w, self.h, arcade.color.ORANGE)

    def update(self):
        if self.vel.y != 0:
            self.pos.add(self.vel)
            self.vel.y = 0

            if self.pos.y >= SCREEN_HEIGHT - self.h / 2:
                self.pos.y = SCREEN_HEIGHT - self.h / 2
            elif self.pos.y <= self.h / 2:
                self.pos.y = self.h / 2

class Ball:
    def __init__(self):
        self.pos = Vector(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.vel = Vector(3, 3)
    
    def draw(self):
        arcade.draw_point(self.pos.x, self.pos.y, arcade.color.RED, 10)

    def update(self, left_pos, right_pos):
        if self.pos.y <= 5:
            self.pos.y = 5
            self.vel.y = 3
        elif self.pos.y >= SCREEN_HEIGHT - 5:
            self.pos.y = SCREEN_HEIGHT - 5
            self.vel.y = -3

        if self.pos.x <= 5:
            self.pos.x = 5
            self.vel.x = 3
        elif self.pos.x >= SCREEN_WIDTH - 5:
            self.pos.x = SCREEN_WIDTH - 5
            self.vel.x = -3

        rect_left = ((left_pos.pos.x - left_pos.w / 2, left_pos.pos.y - left_pos.h / 2),
                    (left_pos.pos.x - left_pos.w / 2, left_pos.pos.y + left_pos.h / 2),
                    (left_pos.pos.x + left_pos.w / 2, left_pos.pos.y + left_pos.h / 2),
                    (left_pos.pos.x + left_pos.w / 2, left_pos.pos.y - left_pos.h / 2))

        rect_right = ((right_pos.pos.x - right_pos.w / 2, right_pos.pos.y - right_pos.h / 2),
                    (right_pos.pos.x - right_pos.w / 2, right_pos.pos.y + right_pos.h / 2),
                    (right_pos.pos.x + right_pos.w / 2, right_pos.pos.y + right_pos.h / 2),
                    (right_pos.pos.x + right_pos.w / 2, right_pos.pos.y - right_pos.h / 2))

        self.pos.add(self.vel)


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

        self.paddle_left = Paddle(True)
        self.paddle_right = Paddle(False)

        self.ball = Ball()

        self.is_w_pressed = False
        self.is_s_pressed = False
        self.is_up_pressed = False
        self.is_down_pressed = False
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.paddle_left.draw()
        self.paddle_right.draw()

        self.ball.draw()

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.is_w_pressed == True:
            self.paddle_left.vel = Vector(0, 5)
        elif self.is_s_pressed == True:
            self.paddle_left.vel = Vector(0, -5)

        if self.is_up_pressed == True:
            self.paddle_right.vel = Vector(0, 5)
        elif self.is_down_pressed == True:
            self.paddle_right.vel = Vector(0, -5)

        self.paddle_left.update()
        self.paddle_right.update()

        self.ball.update(self.paddle_left, self.paddle_right)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.W:
            self.is_w_pressed = True
        elif key == arcade.key.S:
            self.is_s_pressed = True
        elif key == arcade.key.UP:
            self.is_up_pressed = True
        elif key == arcade.key.DOWN:
            self.is_down_pressed = True
    

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.W:
            self.is_w_pressed = False
        elif key == arcade.key.S:
            self.is_s_pressed = False
        elif key == arcade.key.UP:
            self.is_up_pressed = False
        elif key == arcade.key.DOWN:
            self.is_down_pressed = False

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()