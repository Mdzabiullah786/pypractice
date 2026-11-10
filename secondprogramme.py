# to know which type of data is saved         
'''x=1
print(type(x)) 
x=5.6
print(type(x))
b=2+3j
print(type(b))
a=1,2,3
print(type(a))
#to check how much dat it has consumes
import sys
x=15
print(sys.getsizeof(x))
a=67
print(sys.getsizeof(x))
x=45798
print(sys.getsizeof(x))
#print when we increase digit (not number of same digit and also in one condition when no of digit is comparable{not digit differene may be 1,2 or 3,4,5 may be } in int data type then data size will increase in bytes.
x=12.56
print(sys.getsizeof(x))
a=12.567890
print(sys.getsizeof(a))
# now we can say that the memory size of floating value of any no of digit is 24 bytes
x=a+6j
print(sys.getsizeof(x))
c=a+897j
print(sys.getsizeof(c))
# we can say that for any no of digit in complex the memory size will remain same that is 32 bytes.
# to calculate index letter by using index no. of that by seeing the value from index table.'''
x=("hello python")
print(x[8])
print(x[4:9])
print(x[:4])
print(x[4:])
print(x[1:9:2]) # it will print from 1 to 9 but it will skip one letter after printing one letter.
print(x[:4:2]) # it will print from 0 to 4 but it will skip one letter after printing one letter.
print(x[::-1]) # it will print in reverse order

str='welcome to python\'s world'
print(str)
str="welcome to python's world"
print(str)  
print("I am fresher also")
# docstring 
"""
 hello world  
   this is not going to happen
              i will score
"""
# multi line string  
a="""my name
salim 
 zabiullah"""
print(a)
# logical operators
print(not False)
a=4
b=3
print (not (a > b))
val1=True
val2= False
print("AND operator:",val1 and val2)
# and operator evaluate all condition and give the decision after evaluating over all an print second option
print("OR operator:",val1 or val2)
print("OR operator:",(a==b) or (a>b))
# or operater  evaluate all  the situation amongst all that is best which will give as operator output.
# type conversion 
a = 2
b = 4.25
sum= a+b #it will treat 2 as floating vlue (2.0) when we add with floating value  
print(sum)
# str+ float = error
# type casting(we only can type casting when characters are from same family so that it can fit in)
a=float("2")
b= 4.25
print(a + b)
a = 3.14
a = int(a)

print(type(a))
name=input("entetr your name")
print("welcome ",name)
val=input("enter some value: ")
print(type(val),val)
int("5")
val = float(input("enter some value :"))
print(type(val),val)
name=input("enter your name")
age=input(" enter your age")
marks=input('enter your marks')
# we can convert or change the data type by putting the data type before input that we want to convert for eg (float/int/complex/tuple )
print("my name is",name)
# print use of (\n)
print("\n") # it will create a little space b/w two sentence or print("\x") x can be anything it work as same as print("\n")
print("heloo\n world")






