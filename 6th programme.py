# control flow statement
# Match case statement is a control flow statement that allows you to execute different blocks of code based on the value of a variable or expression. It is similar to the if-elif-else statement, but it can be more concise and easier to read when dealing with multiple conditions.
'''day=input("enter the day of the week:")
match day:
    case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
        print("It's a weekday!")
    case "Saturday"|"Sunday":
        print("It's the weekend!")
    case _:
        print("Invalid day!")

day=int(input("enter the day of the week:"))
match day:
    case 1:
        print("It's Monday!")
    case 2:
        print("It's Tuesday!")
    case 3:
        print("It's Wednesday!")
    case 4:
        print("It's Thursday!")
    case 5:
        print("It's Friday!")
    case 6:
        print("It's Saturday!")
    case 7:
        print("It's Sunday!")
    case _:
        print("Invalid day!")

# making calculator using match case statement
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
operation=input("enter the operation (+, -, *, /):")

match operation:
    case "+":
        result=num1+num2
        print(f"The result is: {result}")
    case "-":
        result=num1-num2
        print(f"The result is: {result}")
    case "*":
        result=num1*num2
        print(f"The result is: {result}")
    case "/":
        if num2 != 0:
            result=num1/num2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation!")'''
 
#loop statement
# A loop statement is a control flow statement that allows you to execute a block of code repeatedly based on a condition. There are two main types of loop statements in Python: for loops and while loops.
# while loop [note-: in while loop iterative step always comes in the last and before exiting loop.] 
'''count=0 # initializing the count variable
while count <= 5:
    print(f"Count: {count}")
    count += 1 # incrementing the count by 1 in each iteration
i=6
while i>=1:
    print(i)
    i-=1 # decrementing the i by 1 in each iteration

count=0 # initializing the count variable
while count <= 5:
    print(f"Count: {count}")
    count += 2 # incrementing the count by 2 in each iteration

count=0  # initializing the count variable
s=2 # initializing the sum variable in this case continuous no . are not going  to be added continuously.
while count <= 5:
    print(f"Count: {count}")
    count += 2
    s += 2 # incrementing the s by 2 in each iteration
    print(f"Sum: {s}")
# infinite loop is a loop that runs indefinitely, without a termination condition. It can be created using a while loop with a condition that always evaluates to True. Infinite loops can be useful in certain scenarios, such as when you want to continuously listen for user input or perform background tasks. However, they should be used with caution, as they can lead to unresponsive programs if not properly managed.
while True:
    print("This is an infinite loop. Press Ctrl+C to stop it.")
# print increasing numbers in an infinite loop
i=0
while True:
    print(i)
    i += 1
# be careful while printing even numbers.it is wrong for printing even numbers because it will print the even numbers and also the odd numbers because the print statement is inside the if statement. so it will print the num variable in each iteration of the loop, regardless of whether it is even or odd.
num=0
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1
    print(f"num: {num}") # printing the num variable after incrementing it by 1 in each iteration

# even numbers.method 1
num=0
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1
# even numbers.method 2 without using if statement
num=0
while num <= 10:
    print(num)
    num += 2
# summation of series using while loop (standard method)
 # instead taking user input for n, we can also define a fixed value for n. For example, we can set n=10 to calculate the sum of the first 10 natural numbers. This way, we can avoid any potential errors that may arise from user input and ensure that the program runs smoothly.
sum=0
i=1
while i <10 :
    sum += i
    i += 1
print(f"The sum of the series is: {sum}")# print() should be outside the while loop because we want to print the final sum after the loop has completed, not during each iteration of the loop. If we put the print() statement inside the while loop, it would print the sum at each iteration, which is not what we want. By placing it outside the loop, we ensure that it only prints once, after all iterations are complete and the final sum has been calculated.
# how to control infinite loop'''
'''i=0
while True:
    print(i)
    i+=1
    if i>10:
        break

# concept of if, else, break
while True:
    user_input=input("enter'exit' to stop loop: ")
    if user_input.lower() == 'exit':
        print("exiting loop.")
        break
    else:
        print(f"you enterd:{user_input}")
# print table using while loop [V.V.I]
num=int(input("enter the number to print its table:"))
i=1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1'''
# while loop in list ( sequencial traverse through the list)
####################### IMPORTANT REVISE BEFOREW EXAM ######################
'''nums=[1,2,3,4,5]
i=0
while i < len(nums):
    print(nums[i])
    i += 1
## while loop in tuples
nums=(1,2,3,4,5,6,7,8,9,5)
x=5
i = 0
while i < len(nums):
    if nums[i] == x:
        print("found at index:",i)
    else:
        print("finding......")
    i += 1

nums=(1,2,3,4,5,6,7,8,9,5)
x=int(input("enter the number to find its index:"))
i=  0
while i < len(nums):
    if nums[i] == x:
        print("found number at idx:", i)
        break # it break the iteration or stop the iteration.
#will terminate the loop after reaching condition.
    else:
        print("finding.....")# it will not print finding, once we found number at i.
        i+=1
print(" terminated. because we have use break , so this is end of loop")

 # continue in while loop 
i=0
while i<=10:
    if(i%2 == 0):
        i+=1
        continue # it will skip the value that we want.for eg here we have skip even no.
    print(i)
    i+=1
# use of for loop
li=[1,2,3,4,5]
for el in li:
    print(el)
else:
    print("EENNNNNNNNNNNNNND")
str=("lovely proffesional university")
for chr in str:
    if (chr =='u'):
        print('u found')
        break
    print(chr)
else:#  after using else it will no print end here.when we use break then we use else .
    print("END")
print("="*80)

text=("lovely proffesional university")
for chr in text:
    if (chr =='u'):
        print('u found')
        print(chr)
else:
    print("END") 

li=[int(i) for i in input().split(",")]
print(li)
################################# V.V.I #####################################
# Sum of the digit
y= str(input())# here force fully we r using type conversion because  for loop does not traverse on a integer sequence.
s=0
for i in y:
    s+=int(i)
print(s)# sum of the digit'''
# n= int(input())
# s=0
# for i in range(1,n+1):
#     s+=int(i)
# print(s)

'''n=int(input())
fact=1
for i in range(1,n+1):# in rage we have use 1, n+1 it means it goes forward 1*2*3*4*5
    fact*=i
print("Factorial:",fact)
n= int(input())
fact=1
for i in range(n,0,-1): # here it count down ward as 5*4*3*2*1
    fact*=i
print("Factorial:",fact)
#### 3rd version ####
n=int(input())
fact=1
for i in range(1,n+1):# in rage we have use 1, n+1 it means it goes forward 1*2*3*4*5
    fact*=i
    print("Factorial:",fact)# it will print all factorial  of digit from 1 to n 
    #################  IMPORTANT  ################
r=int(input())
for i in range(1,r+1):
    print("*"*i)
r=int(input())
for i in range(r,0,-1):
    print("*"*i)
# print sum of the table 
t=int(input())
s=0
for i in range(1,11):
    s += t * i
print(s)
t=int(input())
s=0
for i in range(1,11):
    s = t * i
    print(s)
k=int(input())
m=0
for i in range(1,11):
    print(f"{k}*{i}={k*i}")
# nesting of while loop'''



#indentify operators
'''a = -8# here it is true showing because of constant folding ( because we have allready assighn and both are same at diiferent memory so python locate in same memory.)
b = -8
print(a is b)

a=int(input()) # here when we take user input same in both and b that show same value provided that user input should be lie in this range [-5,256] in case of [257,infinity) or (-infinity, -5) it will treat as two different value so it will stored in two different memory hence both are differnt.
b= int(input())# python does not do scope wise optimisation for small integer cache which is [-5,256]
print(a is b)'''
# SUM OF DIGIT USING WHILE LOOP 
n=int(input("4dgt no:"))
s=0
while n>0:
    d = n%10
    s+=d
    n = n//10
print(s)
 #######################################  V.V.I  #######################################
x = int(input())
l=0
while x>0:
    d=x%10
    if d > l:
        l=d
    x = x//10
 #   print("the large no is:",l) print() must be out side the loop otherwise it will print each iteration of the loop
print("the larger no is:", l)
n = int(input()) 
l =  len(str(n)) 
temp=n
s=0
while n>0 :  
    d=n%10
    s+=d**l
    n=n//10
if s == temp:
    print(" this is arms trong number becz sum:",s)
else:
    print("not a arm strong no. becz sum:",s )









