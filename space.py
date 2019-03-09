"""
Sprite Move With Keyboard

Simple program to show moving a sprite with the keyboard.
The sprite_move_keyboard_better.py example is slightly better
in how it works, but also slightly more complex.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard
"""

import arcade
import os
import random

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

MOVEMENT_SPEED = 200


class Player(arcade.Sprite):

    def __init__(self, path, scaling=1):
        super().__init__(path, scaling)

        self.lasers_list = arcade.SpriteList()
        self.shield = arcade.Sprite("images/PNG/Effects/shield3.png", 0.7)
        self.lives = 3

    def shot(self):
        laser = LaserShot("images/PNG/Lasers/laserBlue07.png")
        laser.center_x = self.center_x
        laser.center_y = self.center_y + self.height // 2 + laser.height // 2

        self.lasers_list.append(laser)

    def damage(self, asteroid):
        asteroid.kill()
        if self.shield != None:
            self.shield = None
            return True

        self.lives = self.lives - 1
        return self.lives > 0



    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

        if self.shield != None:
            self.shield.center_x = self.center_x
            self.shield.center_y = self.center_y

class LaserShot(arcade.Sprite):

    def update(self):
        self.center_y = self.center_y + self.change_y

        if self.bottom > SCREEN_HEIGHT:
            self.kill()

class HitEffect(arcade.Sprite):

    def __init__(self, path, scale=1):
        super().__init__(path, scale)
        self.timer = 0.0

    def update(self):
        if self.timer >= 0.1:
            self.kill()

class Asteroid(arcade.Sprite):
    def __init__(self, path, scale=1):
        super().__init__(path, scale)
        self.lives = 3
    
    def update(self):
        self.angle = self.angle + 1
        self.change_y = 1
        self.center_y = self.center_y - self.change_y

        if self.top < 0:
            self.kill()

    def hit(self):
        self.lives = self.lives -1
        if self.lives <= 0:
            self.kill()

class AsteroidSpawner:
    def __init__(self):
        self.timer = 0.0
        self.asteroids = arcade.SpriteList()

    def update(self, delta):
        self.timer = self.timer + delta

        if self.timer > random.uniform(1.3, 2.0):
            self.timer = 0.0
            if len(self.asteroids) <= 15:
                self.create_asteroid()

    def create_asteroid(self):
        asteroid = Asteroid("images/PNG/Meteors/meteorGrey_big2.png", 0.4)

        asteroid.center_y = SCREEN_HEIGHT + asteroid.height // 2
        asteroid.center_x = random.randint(0, SCREEN_WIDTH)

        self.asteroids.append(asteroid)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.is_left = False
        self.is_right = False

        self.background_sprite = None

        self.is_shot_needed_ = False
        self.shot_timer = 0.0
        self.spawner = None

        self.effects = None
        self.is_started = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = Player("images/PNG/red.png", SPRITE_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.background_sprite = arcade.Sprite("images/Backgrounds/purple.png", 3.3)
        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2

        self.spawner = AsteroidSpawner()

        self.effects = arcade.SpriteList()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.is_started == False:
            arcade.draw_text(
                "Нажмите пробел для новой игры",
                100,
                SCREEN_HEIGHT // 2,
                arcade.color.ANDROID_GREEN,
                20)
            return

        self.background_sprite.draw()

        # Draw all the sprites.
        self.player_list.draw()
        if self.player_sprite.shield != None:
            self.player_sprite.shield.draw()

        self.player_sprite.lasers_list.draw()
        self.spawner.asteroids.draw()

        self.effects.draw()

        arcade.draw_text(
            "Жизни: {}".format(self.player_sprite.lives),
            10,
            SCREEN_HEIGHT - 30,
            arcade.color.ANDROID_GREEN,
            20
        )

    def update(self, delta_time):
        """ Movement and game logic """

        if self.is_started == False:
            return

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        if self.is_right == True:
            self.player_sprite.change_x = MOVEMENT_SPEED * delta_time
        elif self.is_left == True:
            self.player_sprite.change_x = -MOVEMENT_SPEED * delta_time

        self.player_list.update()

        for laser in self.player_sprite.lasers_list:
            laser.change_y = MOVEMENT_SPEED * delta_time
        
        self.player_sprite.lasers_list.update()

        if self.shot_timer > 0.0:
            self.shot_timer = self.shot_timer - delta_time

        if self.is_shot_needed_ == True and self.shot_timer <= 0.0:
            self.player_sprite.shot()
            self.shot_timer = 0.3

        self.spawner.update(delta_time)
        self.spawner.asteroids.update()

        bullets_to_delete = []
        for bullet in self.player_sprite.lasers_list:
            asteroids_col = arcade.check_for_collision_with_list(bullet,
                                                        self.spawner.asteroids)
            for asteroid in asteroids_col:
                asteroid.hit()

            if len(asteroids_col) > 0:
                bullet.kill()
                hit_effect = HitEffect("images/PNG/Lasers/laserBlue10.png", 0.8)
                hit_effect.center_x = bullet.center_x
                hit_effect.center_y = bullet.top
                self.effects.append(hit_effect)
            
        for effect in self.effects:
            effect.timer = effect.timer + delta_time
        
        self.effects.update()

        asteroids_col = arcade.check_for_collision_with_list(
            self.player_sprite,
            self.spawner.asteroids
        )

        for asteroid in asteroids_col:
            self.is_started = self.player_sprite.damage(asteroid)
            effect = HitEffect("images/PNG/Lasers/laserBlue10.png", 0.8)
            effect.center_x = self.player_sprite.center_x
            effect.center_y = self.player_sprite.top
            self.effects.append(
                effect
                )
        
        if self.is_started == False:
            self.player_sprite.lives = 3
            self.spawner.asteroids = arcade.SpriteList()



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.LEFT:
            self.is_left = True
        elif key == arcade.key.RIGHT:
            self.is_right = True
        
        if key == arcade.key.SPACE:
            if self.is_started == True:
                self.is_shot_needed_ = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
            self.is_left = False
            self.is_right = False
    
        if key == arcade.key.SPACE:
            if self.is_started == True:
                self.is_shot_needed_ = False
            else:
                self.is_started = True



def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()