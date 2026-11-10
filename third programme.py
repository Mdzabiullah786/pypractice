 # practice
'''a=int(input())
b=int(input())
sum=(a+b)
print(a+b)
side=float(input("square's side"))
print("area=", side *side )
a=int(input())
b=int(input())
average=((a+b)/2)
print(average)
a=int(input()) 
b=int(input())
print(a>=b)
str1="zbh"
len1=len(str1)
print(len1)
str2="name"
len2=len(str2)
print(len2)
final_str=str1 +" " + str2
print(final_str)
print(len(final_str))
# use of string function .
str= "i am studying python from lpu"
print(str.endswith("pu"))
print(str.capitalize())
str=(str.capitalize())# to get change in original stringother wise it will create changes newer string(it make newer string to change )
print(str)
print(str.replace("a","b"))
print(str.replace("lpu","iit"))
print(str.find("o"))# find posn of character in string
print(str.find("q"))# here q is not belongs to our given string that's why it will give u -1 (negative index only use in slicing)
print(str.count("o"))# it will calculate the occurence of string or character
# use of if/elif/ese
# if is used for block or creating condn.
age=24
if (age>=18):
    print("can vote")
    print("can drive")
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):# we use elif when ever if condn.fails then elif will come in picture.(it ise useful only after"if",once elif detected the statement true then it will not move further )(else+if=elif) # elif use in between else and if to add multiple condn.
    print("go")
# we use else with if or elif or both(else will come in picture when else and elif fail or may be one fail out of two ,note else always use at the end of condn.)
age=24
if(age>=18):
    print('can vote')
else:
    print("can't vote")
marks=int(input("enter your marks:"))# dont forget semicolon(:)
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade= "C"
else:
    grade="D"
print("grade of the student ->",grade)
marks=[2,3,4,5,6,7,8]
print(list(marks))
print(marks)
print(type(marks))
print(marks[4])
print(marks[1:5])

print(ord("a"))
L1=[1,3,5,7,9]
L2=[2,4,6,8,10]
print(L1+L2)
print(2*L2)'''

# list=[2,3,1]
# print(list.sort())# it will  give none
# list=[2,3,1] # we r using index no
# list.append(4)
# print(list) # it will append 4 in the last without arranging.
# print(list.append(4)) # it will  give u none because append is a method which will not return any value it will only modify the list
# list.sort()
# print(list) # here do two thing at a time one sorting and apend 4 also because we have earlier use append method before sort method 
# # to arrange in descendig order
# print(list.sort(reverse=True))# here it will give none because uysing print
# print(list)# here it will print list after sorting & reversing & append also
print(sorted(list)) # it will print a new list after sorting & it always return list whether it is any data type (list/tuple) but it will not modify the original list or tuple
print(list) # it will print original list because sorted is a function which will return a new list after sorting but it will not modify the original list

'''list=[1,2,3]
list.append(4)
list.reverse()
print(list) # it will first append 4 and then it will do reverse in same output
list=[2,1,3]
list.insert(1,5)#1 is idx no. & 5 is elmnt which we hve to insert 
print(list)
list.extend([1,5])
print(list)
list=[2,1,3,1]
list.remove(1)# remove first occurence of 1 and it will not return any value or remove first matching element from the list whether occurremce is 1 or more than 1 it will remove first occurence only
print(list)
list.pop(2) # 2 is idx no. which we hve remove elmnt of tht idx,and it will return the removed element that we can store in any variable
print(list)'''
# # nesting of list
# list=[1,2,[3,4],5,6]# lenth=5
# print(list[2])
# print(list[1])
# print(list[2][0])
# print(len(list))
# tuple
tup=(1,)
print(tup)
print(type(tup))
# slicing of tupple 
# tp.index(element)
# tup.count(element)
sup=(1,2,3,4,)
print(sup.index(2)) # 2 is element fr which r finding index
print(sup.count(2)) # count no of occurences
# conversion of tuple to list or list to tuple 
bup=(1,2,3,4,5)
print(type(bup))
du = list(bup)
print(du)
print(type(du))
# list to tuple
cup=[1,2,3,4]
print(type(cup))
suv=tuple(cup)
print(suv)
print(type(suv))




    