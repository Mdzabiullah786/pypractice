# while loop without any new iterative step so it will print only zero Infinite times because there is no any iterative step.
# a=0
# while a<5:
#     print(a)
# calculator in very simple way without using any condition and control flow statement.
'''a=input("float/integer: ")
b= input("float/integr: ")
c= input("use operators:+,-,*,/): ")
result = eval(str(a)+c+str(b))
print("result:", result )
print(type(result))'''
# in this case it will excute a in a loop up to end.and then print final sum upto end
'''a=1 # a ko upere likhon ya niche koi farak nahi padta hai same b ko bhi kahi likh sakte hai
b=0
while a < 10:
    print(a)
    b+=a
    a+=1
print(b)
# in this case excute a first in a Loop along with that it add upto end and then print sum upto end
a=1
b=0
while a < 10:
    print(a,end="+" if a < 9 else"=")
    b+=a
    a+=1
print(b)
# # in this case it will print continuous 
a=1
b=0
while a < 5:
    print(a)
    b+=a
    a+=1
print(a)# it is playig role to print after exiting loop because it is outside the loop when a becomes 5 print funcn inside the loop will not print but one print function is outside the loop so it will print 5.

a=1
b=0
while a < 5:
    print(a)
    a+=1
    b+=a
print(b) # it is same as previous print funcn outside the loop so it will print  (b) of last iteration of after exiting loop
a=1
b=0
while a < 5:
    a+=1
    b+=a
print(b)'''
 # NESTING OF FOR LOOP #
'''for i in range(4):
    for j in range(i):
        print(j,i) 
print("other way")
for i in range(4):
    for j in range(3):
        print(j,i)
# print table usin nesting 
  
for i in range(1,4):
    print(f"table{i}") # here it is use to print heading of table such as table 1, table 2, & table 3 and so on.
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print()

print("other way ")
n =4
for i in range(1,n):
    print(f"table{i}")
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print()
###########################################################################
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print() # to create other line for execution
#########################################################################
k= int(input())
for i in range(1,k+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
##########################################################333333333
n=int(input())
s=0
i=0
while i<=n:
    s+=i
    i+=2
print(s)
n=int(input())
for i in range(1,n+1):
    print(i)
n=int(input())
s=0
i=0
while i<=n:
    s+=i
    i+=2
    print(s)   
#############################################33333######################
str
a = float(input())
b = float(input())
if a > b and b == 0:
    print("undefined")
elif a > b:
    print(f"{a}/{b}={a/b:.1f}")
elif b > a:
    print(f"{a}*{b}={a*b:.1f}")'''
# print table
n = int(input())
p = int(input())
for i in range(1,n+1):
    print(p*i)
    


 
