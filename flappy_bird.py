"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

class Bird:
    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.size = 20

    def draw(self):
        arcade.draw_point(self.pos.x, self.pos.y, arcade.color.RED_PURPLE, self.size)

    def apply_force(self, force):
        self.acc.add(force)

    def update(self):
        self.vel.add(self.acc)

        self.max_vel()

        self.pos.add(self.vel)

        self.acc = Vector(0, 0)

        if self.pos.y >= SCREEN_HEIGHT - self.size // 2:
            self.pos.y = 1 + self.size // 2

    def max_vel(self):
        if self.vel.y > 8:
            self.vel.y = 8
        elif self.vel.y < -8:
            self.vel.y = -8

    def get_points(self):
        points = (
            (self.pos.x - self.size // 2, self.pos.y - self.size // 2),
            (self.pos.x - self.size // 2, self.pos.y + self.size // 2),
            (self.pos.x + self.size // 2, self.pos.y + self.size // 2),
            (self.pos.x + self.size // 2, self.pos.y - self.size // 2)
        )
        return points

class Tube:
    def __init__(self, h, w, pos, color):
        self.pos = pos
        self.color = color
        self.h = h
        self.w = w
        self.need_delete = False

    def draw(self):
        arcade.draw_rectangle_filled(self.pos.x, self.pos.y,
                                     self.w, self.h, self.color)

    def update(self):
        self.pos.add(Vector(-2, 0))
        if self.pos.x < 0 - self.w // 2:
            self.need_delete = True

    def get_points(self):
        points = (
            (self.pos.x - self.w // 2, self.pos.y - self.h // 2),
            (self.pos.x - self.w // 2, self.pos.y + self.h // 2),
            (self.pos.x + self.w // 2, self.pos.y + self.h // 2),
            (self.pos.x + self.w // 2, self.pos.y - self.h // 2),
        )
        return points


class SpawnerTube:
    def __init__(self):
        self.tube_list = []
        self.timer = 0.0

    def update(self, time):
        self.timer = self.timer + time
        if self.timer >= 2.0:
            offset = random.randrange(-70, 70)
            self.tube_list.append(Tube(400, 100,
                                  Vector(SCREEN_WIDTH + 50, SCREEN_HEIGHT + offset),
                                  arcade.color.WHITE))

            self.tube_list.append(Tube(400, 100,
                                  Vector(SCREEN_WIDTH + 50, 0 + offset),
                                  arcade.color.WHITE))

            self.timer = 0.0

    def get_tubes(self):
        return self.tube_list

class Label:
    def __init__(self, x, y, text, size):
        self.x = x
        self.y = y
        self.text = text
        self.size = size

    def set_text(self, text):
        self.text = text

    def draw(self):
        arcade.draw_text(self.text, self.x, self.y,
                         arcade.color.YELLOW, self.size)


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

        self.is_need_jump = False

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        self.bird = Bird(Vector(100, SCREEN_HEIGHT // 2))
        self.spawner = SpawnerTube()

        self.start_timer = Label(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                 '3', 80)

        self.is_new_game = True
        self.new_timer = 4.0

    def start_new_game(self):
        self.is_new_game = True
        self.bird = Bird(Vector(100, SCREEN_HEIGHT // 2))
        self.spawner.get_tubes().clear()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        if self.is_new_game == True:
            self.start_timer.draw()

        self.bird.draw()

        for tube in self.spawner.get_tubes():
            tube.draw()
        

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.is_new_game == True:
            self.new_timer = self.new_timer - delta_time
            self.start_timer.set_text(str(int(self.new_timer)))

            if self.new_timer <= 0.0:
                self.is_new_game = False
                self.new_timer = 4.0
            return

        if self.is_need_jump == True:
            self.bird.vel = Vector(0, 4)

            self.is_need_jump = False

        gravity = Vector(0, -0.2)
        self.bird.apply_force(gravity)

        self.bird.update()

        self.spawner.update(delta_time)

        deleted_tubes = []
        for tube in self.spawner.get_tubes():
            tube.update()
            if tube.need_delete == True:
                deleted_tubes.append(tube)

        need_start_new_game = False

        for tube in self.spawner.get_tubes():
            bird_points = self.bird.get_points()
            tube_points = tube.get_points()
            collision = arcade.are_polygons_intersecting(bird_points,
                                                         tube_points)
            if collision == True:
                need_start_new_game = True
                break

        for tube in deleted_tubes:
            self.spawner.get_tubes().remove(tube)

        if self.bird.pos.y <= 0:
            need_start_new_game = True

        if need_start_new_game == True:
            self.start_new_game()



    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.SPACE:
            self.is_need_jump = True

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