class Mammal:
    def speak(self):
        print("HI")
class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

dog = Dog();
dog.speak()
Cat().speak();
