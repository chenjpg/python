# class Student(object):
#     def get_score(self):
#         return self.__score
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100!')
#         self.__score = value

# s = Student()
# s.set_score(60)
# print(s.get_score())
# s.set_score(100000) 会报错

class Student(object):
    @property
    def birth(self):
        return self.__birth# birth 这是因为调用s.birth时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，于是又转换为方法调用self.birth()，造成无限递归，
    # 最终导致栈溢出报错RecursionError。
    @birth.setter
    def birth(self,value):
        self.__birth = value

    @property
    def age(self):
        return 2026- self.__birth
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self.__score = value
s = Student()
s.score = 60
print(s.score)
# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。


s.birth = 2001
print(s.age)