'''class Animal:
    def sound(self):
        print("here goes the sound")

class dog(Animal):
    def sound(self):
        print("woof")


class cow(Animal):
    def sound(self):
        print("moo")

class pom(dog):
    pass

animals=[Animal(),dog(),cow(),pom()]
for animal in animals:
    animal.sound()
'''



#single level
'''class Animal:
    def sound(self):
        print("here goes the sound")

class dog(Animal):
    def sound2(self):
        print("woof")

obj=dog()
obj.sound()
obj.sound2()'''



#multiple
'''class father:
    fname=""
    def call(self):
        print(self.fname)

class mother:
    mname=""
    def call(self):
        print(self.mname)

class son(father,mother):
    def call(self):
        print("Fathers name"+self.fname)
        print("Mothers name"+self.mname)


hi=son()
hi.fname="joy"
hi.mname="happy"
hi.call()'''



#multilevel

'''class grandfather:
	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

class Father(grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername
		grandfather.__init__(self, grandfathername)

class Son(Father):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)

s1 = Son('rajan', 'soman', 'shashi')
print(s1.grandfathername)
s1.print_name()

'''




#hierarchial inheritance
'''class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print("Vehicle name:", self.name)

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    
    def show(self):
        print("Car name:", self.name)

class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    
    def show(self):
        print("Truck name:", self.name)


car_obj = Car("Porsche")
truck_obj = Truck("Tata")

car_obj.show()
truck_obj.show()  
'''


#Hybrid inheritance

'''consisting of every inheritance'''



#MEthod overriding
'''class shape:
    def area(self):
        raise NotImplementedError
    
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        print(self.l*self.b)


r=rectangle(5,5)
r.area()'''
    