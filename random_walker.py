import arcade
import random

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_WIDTH // 2

class RandomWalker:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_point(self.x, self.y, arcade.color.RED, 20)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Random walker")
        self.walker = RandomWalker(200, 200)

    def on_draw(self):
        arcade.start_render()
        self.walker.draw()

    def update(self, delta_time):
        pass

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.walker.x = self.walker.x - 10
        
        if key == arcade.key.RIGHT:
            self.walker.x = self.walker.x + 10

        if key == arcade.key.UP:
            self.walker.y = self.walker.y + 10
        
        if key == arcade.key.DOWN:
            self.walker.y = self.walker.y - 10

        if self.walker.x + 20 / 2 > SCREEN_WIDTH:
            self.walker.x = SCREEN_WIDTH - 20 / 2


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()