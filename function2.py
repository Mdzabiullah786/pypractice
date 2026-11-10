# lambda functions are anonymous functions that can take any number of arguments but can only have one expression. They are often used for short, simple functions that are not reused elsewhere in the code. The syntax for a lambda function is as follows: '''lamda parameter_list: expression'''. The expression is evaluated and returned when the lambda function is called. Lambda functions can be assigned to variables, passed as arguments to other functions, and used in higher-order functions like map(), filter(), and reduce(). They are commonly used in situations where a small function is needed for a short period of time, such as in sorting or filtering data
'''marks=list(map(int,input().split()))
result = map(lambda x:x*2,marks)# we use when we have to transform each element in list or tuple
print(list(result))
p = filter(lambda x : x>40,map(lambda x:x*2 ,marks))
d=list(p)
print(d)
# reduce 
from functools import reduce 
q = reduce(lambda x,y : x+y, d)
print(q)'''
# global scoping or local scoping 
'''x = 10

def show():
    print(x)

show()
################################################################
x = 10

def show():
    x = 20
    print(x)

show()
print(x)
################################################################
a = 5

def calculate():
    a = 15
    b = 10
    print(a + b)

calculate()
print(a)'''


'''# Qno 1 update the marks of rahul in subject 
name = "Rahul"
marks = 50
def update_marks():
    global marks 
    marks = 80
    print(f"The marks of {name} is {marks}")
update_marks()
############### lexical *(scoping where inner function cretated)*
x = 100
def first():
    x = 50

    def second():
        print(x)

    second()

first()
################################################################
def father():

    money = 1000

    def child():

        money = 200
        print(money)

    child()

father()
#888888888888888888888888888888888888888888888888888888888888
money = 5000

def father():

    money = 1000

    def child():
        print(money)

    return child


my_function = father()


def uncle():

    money = 200

    my_function()


uncle()''' 
# we wnan to print the sum of digit using recursion only
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + sum_of_digits(n // 10)

# # Example usage
# number = int(input("Enter a number: "))
# print("Sum of digits:", sum_of_digits(number))
# # using recursion we have to build a calculator raises to power of a number
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base * power(base, exponent - 1)

# # Example usage
# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))
# print("Result:", power(base, exponent))
# # using recursion we have to find the factorial of a number 
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Example usage
# number = int(input("Enter a number: "))
# print("Factorial:", factorial(number))
# # using recursion we have to find the fibonacci series of a number
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# # for i in range(number):
# #     print(fibonacci(i), end=" ") we can use this loop to print the fibonacci series of a number but we can also use list comprehension to print the fibonacci series of a number

# # Example usage
# number = int(input("Enter a number: "))
# print("Fibonacci series:", fibonacci(number))
# # gcd of two number using recursion
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# # Example usage
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print("GCD:", gcd(a, b))
#3333333333333333333333333333333333333333333333333#5555555555555555555555555555555555555555555555555555555555555555555555555
# # using math module we can find the gcd of two number using math.gcd() function
# import math
# print("GCD using math.gcd:", math.gcd(a, b))

# A swimming pool is circular and has a radius of 1o meters. the owner wants to calculate the area of and circumference of the pool using mathematical constant
import math
# r = int(input())
# area = math.pi*r**2
# circumference = math.tau*r
# print(f"{area:.2f}")
# print(f"{circumference:.2f}")
# x = int(input("growth rate: " ))
# y = math.e**x
# print(y)
temp =[32,28,35,21,30]
min = math.inf
for i in temp:
    if  min > i:
        min = i
print(min)


marks = [85,90,math.nan,76,math.nan,88]
# marks.remove(math.nan)
# marks.remove(math.nan)
# print(marks)
# print(len(marks))
    
li = []
count = 0
for i in marks:
    if math.isnan(i):
        count+=i
    else:
        li.append(i)
print(count)
print(li)

