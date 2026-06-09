class Student(object):
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def print_age(self):
        print('%s: %s'%(self.name,self.age))
    def get_stage(self):
        if self.age < 8:
            return 'kid'
        elif self.age <18:
            return 'teen'
        else:
            return 'adult'
bart = Student('Bart Simpson',19)
lisa = Student('Lisa', 28)
print(bart.name,bart.age)
def print_age(std):
    print('%s:%s ' % (std.name,std.age))
print_age(bart)
bart.print_age()
print (lisa.get_stage(),bart.get_stage())