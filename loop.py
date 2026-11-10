'''# print prime number( print in same way )
n=int(input())
Flag=True
for i in range(2,n):
    if n%i==0:
        Flag=False
        break
if Flag == True:
    print("prime")
else:
    print("other number")
# method 2
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:# it wii check ony when all the itertative step complete in loop. after exiting loop it will check last one condition or count equation.
    print("Prime")
else:
    print("Not Prime")
# behind the scene of method 2
# let say user input = 3, so, iteration goes upto 4 from 1 
# when i = 1 then 3%1=0 hence, it is true then it will excute count state ment count= count+1(it became count 0+1=1) since  it is not satify count = 2 so, it will not print prime , now it will go in next iteration=2 when i = 2 then 3%2!=0 it is false according to statement so it will not excute next step now again it will go in next itration=3 then 3%3==0 it satisfy so it wil excute next step and now count will becomme 2 finally it will print prime.
# reverse
# find gcd of two number using for loop only
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) 
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
      gcd = i
print("GCD:", gcd)'''


        
    
