__author__ = 'student'
from random import randrange
import random

class shape:
    def __init__(self, h, w):
        self.h = h
        self.w = w


class Triangle(shape):
    def area(self):
        return self.h*self.w/2


class Rectangle(shape):
    def area(self):
        return self.h*self.w


class Mother:
    def __init__(self, word, word2):
        self.word = word
        self.word2 = word2

    def get__repr(self):
        return print(self.word+self.word2)

class Daughter(Mother):
    def __init__(self, word, word2):
        super().__init__(word, word2)


class Animal:
    def  __init__(self, name, age):
        self.name= name
        self.age=age

class Zebra(Animal):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour=colour
    def prints(self):
        print(self.name,':', self.age,',',self.colour)
        return

class Dolphin(Animal):
    def __init__(self, name, age, kind):
        super().__init__(name, age)
        self.kind=kind
    def prints(self):
        print(self.name,':',self.age,',',self.kind)
        return ''

if __name__=="__main__":
    x=randrange(1, 13)
    y=randrange(1, 13)
    T=Triangle(x, y)
    R=Rectangle(x, y)
    print ('Площадь треугольника:', T.area(), 'Площадь прямоугольника:', R.area()) #мухахашечки

    word= ' La'
    word2= '-la'
    word3= '-la!'
    m=Mother(word, word3)
    d=Daughter(word, word2+word3)
    m.get__repr()
    d.get__repr() #пострадать фигней:выполнено


    cl=['More black than white','More white than black', 'Checkerboard']
    kl= ['Sea', 'River', 'Alien', 'Shark']
    c=random.choice(cl)
    k=random.choice(kl)
    z=Zebra('  Marty', randrange(1, 13), c)
    d=Dolphin('  Fisher', randrange(1, 13), k)
    z.prints()
    d.prints()
    if d.kind=='Shark':
        print('   Ам-ням-ням!') #аярыбаярыба
