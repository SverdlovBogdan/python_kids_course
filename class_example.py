class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_about_yourself(self):
        print('I am ' + self.name)
        self.say_age()

    def say_age(self):
        print('I am ' + str(self.age) + ' years')

class Dancer(Human):
    def __init__(self, name, age):
        super(Dancer, self).__init__(name, age)

    def dance(self):
        self.move_left_leg()
        self.move_right_leg()

    def move_left_leg(self):
        print('Move left leg!')

    def move_right_leg(self):
        print('Move right leg!')

    def say_about_yourself(self):
        print('I am dancer!')

class Driver(Human):
    def __init__(self, name, age):
        super(Driver, self).__init__(name, age)
    

bob = Human('Bob', 20)
bob.say_about_yourself()

jack = Human('Jack', 30)
jack.say_about_yourself()

mark = Dancer('Mark', 21)
mark.say_about_yourself()
mark.dance()


