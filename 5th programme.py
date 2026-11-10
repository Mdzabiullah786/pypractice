# membership operators "in"or "not in" these operator are use to check whether the element is present or not in data.
'''str="jerry"
print('y'in str)
print('Y' not in str)
print('Y'  in str)
list=[1,2,3,4]
print( 4 in list)
print("5" in list)
# round function:round(number,no. of digits)
# in round function if end value r not given then it will rounnd off into integer .
print(round(7))
print(round(7.41))
print(round(2.666,2))
print(round(2.66678,0))
print(round(7.5))# in case of this means at mid it will give nearest even integer value in return.
print(round(6.5))
print(round(674,2))
print(round(674,0))
print(round(674,-1))# in case of round off we generally considerd as nerest int multiple of 10^(-no. of digits)
print(round(674,-2))      
print(round(674,-3))      
print(round(674,-4))      
print(round(665,-1))
print(round(675,-1)) 
print(round(-8/3))      
print(round(-1.5))      
print(round(-8/3,2))      
print(round(-8/3,-2))   
print(round(674.1012,-2))      
print(round(1212,-2)) '''
# string formating type 1(old version).format method
'''country="India"
name="Zabiullah"
print("my name is {1} and i am from {0}".format(country,name))
print("my name is {0} and i am from {1}".format(country,name))# in this case posn of country and exachange will change becz of exchange serial no.
a=67
b=78
c=a+b
print("{}+{}={}".format(a,b,c))
print("{}>{}={}".format(a,b,a<b))# in this way we can print true or false.
print("is the value of {}>{}={}".format(a,b,a>b))
a=2
b=4
c=a*b
print("{}*{}={}".format(a,b,c))
#why we need of use of f""
# because it was taking too much time and we had to write a lots of code to excute it .
# f"":
name="salim"
country="india"
print(f"my name is {name} and i am from {country}")
s=int(input())  
t=int(input()) 
w=s*t
print(f"{s}*{t}={w:.2f}") 
print(type(f"{s}*{t}={w:.2f}"))
a=float(input())  
b=float(input()) 
c=a*b
print(f"{a}*{b}={c:.2f}")# here is difference in 60 & 61
print(f"{a:.2f}*{b:.2f}={c:.2f}")  
print(type(f"{a}*{b}={c:.2f}"))
## use of seperator and end.
x=56
y=78
print("value of A:",x) 
print("the value ofA: and B:", x,y) 
print(x,y,sep="/") 
print(x,y,sep=">>") 
print(f"A:{x} B:{y}",sep="/")
print(x,end="-")
print(y)
print(y,end="*")
print(x,end="*")
# problem 3
print("_"*50)
print("\n")
print(" Salary Slip")
("\n")
print("_"*50)
name=input("Employee name")
designation=input("designation")
Basic_salary=int(input("Basic_salary"))
Net_salary=int(input("Net_salary"))
print(f"{name}")
print(f"{designation}")
print(f"{Basic_salary}")
print(f"{Net_salary}")
print("\t")
print("-"*50)
a=int(input())
b=int(input())
# c style formating ( for integer we use %d, for floating % f and % s for string)
# note at the end .Xf is used for print  floarting value after decimal. here X can be anybting.
name="salim"
country="india"
lpu=name+country
print("%s   %s=%s"%(name,country,lpu))
print("%s   %s"%(name,country))
print("my name is,%s"%name,"and i am from %s"%country)
khu=float(input("enter floating value1"))
garg=float(input("enter floating value2"))
friend=khu+garg
print("sum= %f+%f=%.2f"%(khu,garg,friend)) # here is difference in 98 and 99.
print("sum= %.2f+%.2f=%.2f"%(khu,garg,friend))'''
'''p=int(input("enter the value1:"))
q=int(input("enter the value2:"))
u=p+q
v=p*q
print("%d+%d=%d\n%d*%d=%d"%(p,q,u,p,q,v)) # use of misslineous comcept.
s=float(input(":F1"))
t=float(input(":F2"))
w=s+t
print("%f+%f=%.3f\n%d*%d=%d"%(p,q,u,s,t,w))''' # use of misslineous concept.
# problem 4
'''i1=input("enter item1:")
i2=input("enter item2:")
i3=input("enter item3:")
q1=int(input("enter quantity1:"))
q2=int(input("enter quantity2:"))
q3=int(input("enter quantity3:"))
p1=float(input("enter pric1:"))
p2=float(input("enter pric2:"))
p3=float(input("enter pric3:"))
t_a=int(input("enter total amount:"))
print("_"*40)
print("Shopping bill")
print("_"*40)
print("Item              Qty                 Price")
print("_"*40)
print("%s                 %d                    %f"%(i1,q1,p1))
print("%s                 %d                    %f"%(i2,q2,p2))
print("%s                 %d                    %f"%(i3,q3,p3))
print("_"*40)
print("total  amount=%d"%(t_a))'''
# arithematic operators
# a==b
# a+b
# a*b
# a!=b{ not equal} 
'''o=5
k=2
print(o**k)
print(o/k)# float division
print(o%k) # it gives reminder
print(o//k) # floor division ( it gives quotient only)
# misclenious concept
a=int(input("enter three digit no here : "))
last= a%10
middle= (a//10)%10
first= a//100
print(last, middle, first)
v="123"
print(v[2], v[1], v[0])
b=input("3 digt no. ")
print(*b[::-1])# it is same as 148 to 152'''
# bitwise operators
a=14
b=20
print(a&b) # multiply  
print(a|b) # add
print(~a)# ~a is same as not bitwise operator= -(n+1)
print(a>>b) # a*2**b
print(a<<b) # a/2**b
print(b<<a) 
print(a^b) # xor (same-same= zero),opposite =1
# assighnment operators( augmented operators)
# num1=21   
# num1+=2
# print(num1)
# # logical operators # use of logical operator is to check the condition and give us true or false output.
# a=23
# b=56
# c=56
# if a>b and a>c:
#     print("A")
# if b>c and b>a:
#     print("B")
# if b>c and c>a:
#     print("c")
# else:
#     print("false")
# # use of and/or/not logical operators
# print(a or b) # if a is true then it will not check for b and it will return a as output.
# print(a and b) # if a is true then it will check for b and it will return b as output.
# print(not a) # it will return false if a is true and it will return true if a is false.
# print(a>b or a>c)
# # identity operators is and is not
# a=23
# b=23
# print(a==b) # it will return true if both a and b are equal.
# print(a is b) # it will return true if both a and b are the same object.
# print(a is not b) # it will return true if both a and b are not the same object.
# My_list=[1,2,3,4] 
# print(1 in My_list) # it will return true if 1 is present in My_list.
# print(5 not in My_list) # it will return true if 5 is not present in My_list.
# tuple1=(1,2,3,4)
# print(tuple1 is My_list) # it will return false because tuple1 and My_list are not the same object.
# check vowels using membership operator
v = input()
if v.lower() in "aeiou":
    print("vowel")
else:
    print("not a vowel")



                                      
        