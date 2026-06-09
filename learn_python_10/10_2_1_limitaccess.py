class Student(object):
    def __init__ (self,name,score):
        self.__name = name #__name mean private
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
bart = Student('Bart Simpson', 59)
print(bart.get_score())
bart.set_score(99)
print(bart.get_score())
# bart.score=99
# print(bart.score)
