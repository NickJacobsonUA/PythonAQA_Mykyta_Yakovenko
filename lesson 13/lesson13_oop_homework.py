# Task 1:
class Dog:

    def __init__(self, size='big', color='black', breed='breedles'):

        self.size = size
        self.color = color
        self.breed = breed

    @classmethod
    def german_shepherd(self, size, color, breed):
        return Dog(size, color, breed)


    @staticmethod
    def say_woof(self):
        print(f'Hello!, I am a {self.size}, {self.color} dog, woof-woof. I am {self.breed}')


dog = Dog.german_shepherd('big', 'black', 'german shepherd')
dog.say_woof(self=dog)

# Task 2:


class Adidas:

    def __init__(self, size, color, brand, type):

        self.size = size
        self.color = color
        self.brand = brand
        self.type = type

    @classmethod
    def sneakers(cls, size, color, brand):
        return cls(size, color, brand, None)

    def sneakers_description(self):
        print('The sneakers are', self.size, self.color, self.brand)

shoes = Adidas.sneakers('big', 'black', 'adidas')
shoes.sneakers_description()








