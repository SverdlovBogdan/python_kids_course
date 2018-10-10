class Dog:
    def __init__(self):
        self.name = ''
        self.age = 0
    
    def set_age(self, age):
        self.age = age
    
    def speak(self, words):
        print(words)
        

my_human = Dog()
print(my_human.age)
my_human.set_age(26)
print(my_human.age)

my_human.speak('asdjkashfksdf')
my_human.speak('Hello, My age is 26')
