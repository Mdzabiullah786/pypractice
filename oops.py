# empty class
'''class Student:
    pass # here we can pass multiple object without any limitation.
s1 = Student()# object or instances,
print(s1) # it will show what is s1 
print(type(s1)) # it will show  the object belongs to which class and which type of object is stored  not show type as object 
print(type(Student)) # it show the what is  Student
# use dir() & __dict__ to show whether the class is empty or full fill with code 
print(dir(Student)) # --> 8 & 9 both will show same output both will show only in built Attributes and nothing extra  
print(Student.__dict__) # when class is not empty the both will show attributes and content in the class.'''
'''class Student:
    pass
s1 = Student()
s1.name = "Md Zabiullah"
s1.section = "EK"
s2 = Student()
s2.name = "salim"
s2.Class = "Eng"
print(s1.name,s1.section,s2.name,s2.Class)# here you can see there we can pass multiple object in empty class'''
# full class 
'''class Student: # class is blue print or sancha in lay man language(using this we create multiple object or define it ) 
    name = "karan"# name = " " both will get updated after when ever you define object variables in object with that data mean priorty(clss > obj).
    marks= 90 # or marks = 0
s1 = Student()
s1.name = "harish"
s1.marks = 80
print(s1.name)
print(s1.marks)
s2 = Student() # student 2 
print(s2.name) # here you can see we have not defining the object for student or s2 then it is not going to be updated it will get data from class what ever we have defining for the object. 
print(s2.marks)
# or we can print like that
print(s1.name,s1.marks,s2.name,s2.marks)
print(dir(Student))
print(Student.__dict__)'''

'''class Student:
    def getdata(self,name,marks):# self is a alias it's not mandatory to use only self it's just for defining the class best practice use self only.
        self.name = name 
        self.marks = marks
    def display(self):
        print(self.name)
        print(self.marks)
s1 = Student()   # Student("karan",90)if i write like this then display method show student("karan",90) thats not we want.
s1.getdata("Karan", 90) # here you can see as i have not use the constructor now i will have to call the function getdata everytime for every students thats the drawback, that's why we use constructor.
s1.display()'''
"""or we can write 
s1 = Student("Karan",90)
print(s1.name)
print(s1.marks) in place of definig function"""
#.................................................here we are going to learn about constructor..................................................
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5default constructor whether you write or not it always present$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
'''class Student:
    def __init__(self):
        pass'''
#==================================================parametarized Constructor=================================================================
'''class Student:
    def __init__(self,name,marks):
       self.name = name
       self.marks = marks 
    def display(self):
      print(self.name)
      print(self.marks)
marks= int(input())
name = input( "name:", )
s1 = Student(name,marks)
s1.display()'''
#  OR we replace display methode code to this without using function.
'''s1 = Student(name,marks)    
print(s1.name, s1.marks)'''
# Q.no 1
class Mobile:
    def __init__(self,Brand,Model,Price):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
Brand = "Nokia"
Model = 2012
Price = 6000
s1 = Mobile(Model,Brand,Price)
print(s1.Model,s1.Price,s1.Brand)
"""or we use function instead writing multiple code
    def display(self):
        print(self.Brand,self.Model,Self.Price)
s1 = Mobile(Brand,Model,Price)
s1.display()"""
#/////////\\\\\\\\\///////\\\\\\\\\\\\\////////////Q.NO2///////////////\\\\\\\\\\\\\\\\\\\/////////////////
'''import math
class Circle:
    def __init__(self,area,circumference):
        self.area = area
        self.circumference = circumference
r = int(input("radius: "))
area = math.pi*r**2
circumference = math.tau*r
s1 = Circle(area,circumference)
print(f"{s1.area:.2f},{s1.circumference:.2f}")'''


"""or we can write like this
import math
class Circle:
    def __init__(self,area,circumference):
        self.area = area
        self.circumference = circumference
        
    def display(self):
        
        print(f"{self.area:.2f}")
        print(f"{self.circumference:.2f}") 
r = int(input())    
area = math.pi*r**2
circumference=math.tau*r
s1 = Circle(area,circumference)
s1.display() """
"""or we can write like this
class Circle:
    def __init__(self,r):
        self.r=r
    def display(self):
        area = math.pi*self.r**2
        circumference = math.tau*self.r
        print(f"{area:.2f},{circumference:.2f}")
s1 = class(r)
s1.display"""
#################################################################################### q.no.3 
'''class Marks:
    def __init__(self,percentage):
        self.percentage = percentage
m1 = int(input())
m2 = int(input())
m3 = int(input())
totmarks = int(input("total marks: "))
percentage = ((m1+m2+m3)/totmarks)*100
s1 = Marks(percentage)
print(s1.percentage)'''
########################OR#########################
'''class Marks:
    def __init__(self,percentage):
        self.percentage = percentage
    def display(self):
        print(self.percentage)
m1 = int(input("m1: "))
m2 = int(input("m2: "))
m3 = int(input("m3: "))
totmarks = int(input("totmarks: "))
percentage = ((m1+m2+m3)/totmarks)*100
s1 = Marks(percentage)
s1.display()'''
#################OOOOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRRRRRRRRRRRR##############################
"""class Marks:
    def __init__(self,m1,m2,m3,totm):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.totm = totm
    def display(self):
        percentage = ((self.m1+self.m2+self.m3)/self.totm) * 100
        print(percentage)
m1 = int(input("m1: "))
m2 = int(input("m2: "))
m3 = int(input("m3: "))
totm = int(input("totmarks: ")) 
s1 = Marks(m1,m2,m3,totm)
s1 .display()"""




        
    