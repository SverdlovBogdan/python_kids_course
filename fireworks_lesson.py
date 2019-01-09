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
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def mult(self, number):
        x = self.x * number
        y = self.y * number

        return Vector(x, y)

class Partical:
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.vel = Vector(0, random.randrange(300, 600))
        self.size = 10
        self.isProcess = True
        self.transparency = 254
        self.color = [random.randint(0, 255), 
                      random.randint(0, 255),
                      random.randint(0, 255),
                      self.transparency]

    def draw(self):
        if self.isProcess == True:
            self.color[3] = self.transparency
            arcade.draw_point(self.pos.x, self.pos.y,
                              self.color, self.size)
    
    def update(self, delta):
        if self.isProcess == True:
            self.pos.add(self.vel.mult(delta))

    def applyForce(self, force):
        self.vel.add(force)



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

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        self.particle = Partical(SCREEN_WIDTH // 2, -10)
        self.particleList = []
        self.smallparticles = []


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.particle.draw()

        for i in self.particleList:
            i.draw()

        for i in self.smallparticles:
            i.draw()

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        if random.randint(0, 100) <= 10:
            self.particleList.append(Partical(random.randint(0, SCREEN_WIDTH), -100))

        gravity = Vector(0, -6)
        gravity.mult(delta_time)

        deleted_list = []
        for i in self.particleList:
            i.applyForce(gravity)
            i.update(delta_time)
            if i.vel.y <= 0 and i.isProcess == True:
                i.isProcess = False
                deleted_list.append(i)
                for k in range(20):
                    small_particle = Partical(i.pos.x, i.pos.y)
                    small_particle.vel = Vector(random.randint(-50, 100),
                                                random.randint(-50, 300))
                    small_particle.size = 5
                    self.smallparticles.append(small_particle)
        
        for i in deleted_list:
            self.particleList.remove(i)
        deleted_list.clear()

        for i in self.smallparticles:
            i.applyForce(gravity)
            i.update(delta_time)
            if i.transparency > 0:
                i.transparency = i.transparency - 2
            if i.pos.y <= 0:
                deleted_list.append(i)
        
        for i in deleted_list:
            self.smallparticles.remove(i)
        deleted_list.clear()



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
        for i in self.particleList:
            i.pos = Vector(random.randrange(0, SCREEN_WIDTH), -100)
            i.vel = Vector(0, random.randrange(400, 600))

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
        self.particleList.append(Partical(x, -100))


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
