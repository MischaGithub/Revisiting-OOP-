#Creating a class dog

class Dog:
    def __init__(self, fur_colour=None, eye_colour=None, breed=None, name=None):
        self.fur_colour = fur_colour
        self.eye_colour = eye_colour
        self.breed = breed
        self.name = name


    def speak(self): #Always include self first in methods
        print("I am a dog! My name is %s! " % self.name)


    def __str__(self):
        return "This is our dog object! His name is %s, and his breed is %s" % (self.name, self.breed)


class SmartDog(Dog):
    def speak(self):
        print("I am a super smart dog, look at me talk! My name is %s" % (self.name))



class NormalDog(Dog):
    def speak(self):
        print("Woof WOOF")



class MuteDog(Dog):
    def speak(self):
        print("...")



doggo = Dog(fur_colour="Gray and white", eye_colour="Blue", breed="Husky", name="Doggo")

doggo.speak()

smart_dog = SmartDog(name="Ninja")
smart_dog.speak()




