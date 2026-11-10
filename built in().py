# What is alias in python  ?
'''it means give the another variable  to the same object that has allready  asighned by other variable ''' 
l1 = [1,2,3,4,5] # assighning 
l2 = l1 # aliashing 
l1.remove(4)
print(l2)
# built in funcn().py


# # list comprehension
# scores=[45,78,90,62,88,70,95]
# high_scores=[score for score in scores if score>75]
# print(high_scores)
# # question no.2
# Salaries=[25000,55000,48000,62000,75000]
# high_salaries=["Eligible" if salary>50000 else "Not Eligible" for salary in Salaries]
# print(high_salaries)
# question no.3 Email validation Extract only the emails which are from gmail.com domain using list comprehension
# emails=["abc@gmail.com", "def@yahoo.com", "ghi@hotmail.com","pqr@gmail.com",]
# gmail_emails=[email for email in emails if email.endswith("@gmail.com")]
# print(gmail_emails)
# # soscial media user name Scenario:convert all the user names to lowercase using list comprehension
# usernames=input("Enter usernames separated by commas: ").split(",")
# lowercase_usernames=[username.lower() for username in usernames]
# print(lowercase_usernames)
# Question no.5 online shoopping discount scenario: apply a 10% discount to all the prices in the list using list comprehension
'''prices=[int(price) for price in input("Enter price:").split(",")]
dprices=[ float(price - ((price) * 0.1))  for price in prices]
print(dprices)'''
# team=[]
# for i in range(5):
#     name,score=input("Enter name and score separated by space: ").split()
#     team.append([name,int(score)])
# scores=[score for name,score in team]
# print(scores)# THIS is only to see list of scores otherwise we can comment it out 
# highest_score=max(scores)
# runner_up_score=max([score for score in scores if score<highest_score])
# result=[name for name,score in team if score==runner_up_score]
# result.sort()
# print(",".join(result))
######### forming matrix and and its transpose using list conversion and  nested for loop #######
# r=int(input("Enter number of rows:"))
# c=int(input("Enter number of columns:"))
# matrix= []
# print("row wise input of matrix elements:")
# for i in range(r):
#     li= list(map(int, input().split()))
#     matrix.append(li)
# print("original matrix:",matrix)
# write your code for transpose here
'''trans=[]
for i in range(c):
    temp_row=[]
    for j in range(r):
        temp_row.append(matrix[j][i])
    trans.append(temp_row)
print("Transpose of the Matrix:",trans)'''
# now we will do the same using list comprehension
# trans1=[[matrix[j][i] for j in range(r)] for i in range(c)]
# print("Transpose of the Matrix using list comprehension:",trans1)


#  function:
# def greet(name):
#     print(f"hi{name}")
#     print("Are you from Cs department")
# greet("jenny")
# greet("ram")
# a = int(input())
# b = int(input())
# def sum(x,y):
#     return a+b
# print(sum(a,b))
'''a = int(input())
b = int(input())
def sum(x,y):
    return a+b
res=sum(a,b)
print(res)'''

# name = input()
# def marks():
#     marks = int(input())
#     print(f"{name} got {marks} marks in mathematics")
# marks()
# print discount using function 
# totalp= int(input())
# def paidp():
#     p = int(input())
#     print( totalp-(totalp*p/100 ))
# paidp()
# a = int(input())
# b = int(input())
# def sum():
#     return a+b
# sum() it wii give blank space as output we have to use print() whether it is inner or outside of the function.
# def greet():
#     print("helllO ! world")
#     print("welcome to python programming")
#     greet() it will give error as it is calling itself and it will go into infinite loop so we have to call it outside of the function.
# def greet():
#     print("helllO ! world")
#     print("welcome to python programming")
# greet()
# def greet(name,age):
#     print(f"Hello {name}, you are {age} years old.")
# greet("Alice", 25)
# def sum(a,b):
#     return a+b
# print(sum(5, 10))
# def square(a):
#     return a*a
# print(square(4))
#######################################################################################*************************
'''num = int(input("Enter a number: "))
def is_even(num):
    return num % 2 == 0
print(is_even(num))
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(5, 10))
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))'''

# p=int(input())
# q=int(input())
# r=int(input())
# flag = True
# def is_prime(*n):
#     for num in n:
#         for i in range(2, num):
#             if num % i == 0:
#                 flag = False
#                 break
#     return flag
# print(is_prime(p, q, r)) in this case it will check only last number if it is prime or not but we want to check all the numbers so we have to use list comprehension and return list of boolean values.
# print([is_prime(num) for num in [p, q, r]]) in function may be it will print list of boolean value after checking all three numbers.
# right code ###############3333333333
# p=int(input())
# q=int(input())
# r=int(input())
# def is_prime(*n):
#     for num in n:
#         flag = True
#         if num < 2:
#             flag = False
#         else:
#             for i in range(2, num):
#                 if num % i == 0:
#                     flag = False
#                     break
#         print(flag)
# print(is_prime(p, q, r))
 # (*) asterisk is used to unpack the list or tuple into individual arguments when calling a function. and  it treats the input as a tuple of arguments. and (**) double asterisk is used to unpack the dictionary into individual keyword arguments when calling a function. and it treats the input as a dictionary of keyword arguments.