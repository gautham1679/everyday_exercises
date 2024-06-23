'''class Cars:
    pass
car1=Cars()'''


''' insatnce varaiable = insatrnce varaiable is specific to the instance or objects we create
.It may have different values for different instance '''

'''class numbers:
    def increase(self):
        if not hasattr(self,'ins'):
            self.ins=100
        self.ins+=1
        return self.ins
    
num1=numbers()
print(num1.increase())
print(num1.increase())
print(num1.increase())'''


'''class variables are common among all insatnces of a class'''



'''class numbers():
    num=100
    def decrease(num):
        numbers.num-=1

    
num1=numbers()
print(numbers.num)
num1.decrease()
print(numbers.num)'''

#normal method
'''class hi:
    def greet(SELF):
        print("hi")


hello=hi()
hello.greet()'''

#static method

'''class maths:
    @staticmethod
    def oddeven(num):
        if num%2!=0:
            return "odd"
        else:
            return "even"


print(maths.oddeven(51))
'''



'''class Vehicle:
    def __init__(self,type,make,year):
        self.type=type
        self.make=make
        self.year=year

car=Vehicle("Car","Porsche","2027")
print(car.make)
'''


'''class Vehicle:
    def __init__(self,type,make,year):
        self.type=type
        self.make=make
        self.year=year

    def __str__(self):
        return f'{self.type,self.make,self.year}'
    
car=Vehicle("Car","Porsche","2027")
print(car)'''



'''class Vehicle:
    def __new__(cls,*args,**kwargs):
        print("New class")
        return super(Vehicle,cls).__new__(cls)
    
    def __init__(self,type,make,year):
        self.type=type
        self.make=make
        self.year=year

car=Vehicle("Car","Porsche","2027")
print(car.make)'''


'''
class Cars:
    def __init__(self):
        self.data=18097890
    
obj=Cars()
print(obj.data)'''

'''
class Cars:
    def __init__(self,value):
        self.data=value

obj=Cars(109890)
print(obj.data)'''



'''class Hi:
    def greet(self,value):
        print(value+" gautham")

hello=Hi()
hello.greet("hello")'''




'''class Car:
    def __init__(self,value):
        self.data=value


    def update(self, other):
        self.data+=other.data

    def __str__(self):
        return f'{self.data}'

hi=Car(10)
hello=Car(30)

hi.update(hello)
print(hi)'''



'''class Car:
    def __init__(self,value):
        self.data=value


    def add(self):
        self.data+=1
        return self

hi=Car(10)

hi.add()
print(hi.data)'''



'''class hi:
    def method(self,arg1,arg2=0):
        print(f"arg1:{arg1}, arg2:{arg2}")


hello=hi()
hello.method(10,309)
'''


'''class cars:
    def __init__(self):
        self.data=7932

    def get(self):
        return self.data
    
    def set(self,value):
        self.data=value
        

hi=cars()
print(hi.get())
hi.set(49)
print(hi.data)'''




'''class Vehicle:
    def __init__(self,type,make,year):
        self.type=type
        self.make=make
        self.__year=year

    def get(self):
        return self.__year
    
    def set(self,value):
        self.__year=value
    
car=Vehicle("Car","Porsche","2027")
print(car.get())
car.set(49)
print(car.get())
'''



class Vehicle:
    def __init__(self):
        self.__hidden_year=0

    def get(self):
        return self._hidden_year
    
    def set(self,value):
        self._hidden_year=value
    
car=Vehicle()
car.set(49)
print(car.get())