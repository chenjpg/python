class Animal(object):
    def run(self):
        print('Animal is running')
    def eat(self):
        print('Animal is eating')
class Dog(Animal):
    def run(self):
        print('Dog is running')
    def bark(self):
        print('dog can bark')
class Cat(Animal):
    def run(self):
        print('Cat is running')
    def catchMouse(self):
        print('cat catch mouse')
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running')
def run_twice(animal):
    animal.run()
    animal.run()
dog = Dog()
dog.run()

cat = Cat()
cat.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
