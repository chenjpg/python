class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixIn(object):
    def eatmeat(self):
        print('eat meat')

class HerbivoresMixIn(object):
    def eatveg(self):
        print('eat vegatable')

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
    pass

class Bat(Mammal,FlyableMixIn,HerbivoresMixIn):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


