'''bup=(1,2,3,4,5)          # tuple to list
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
# tuple qestion
name = print(input("enter your name"))
email_id=print(input())
anual_salary=print(12*(int(input("enter your salary"))))
tup=(name,anual_salary,email_id)
print(tup[1])
print(tup[2])
# question 2
X_co_ordinate=int(input("x="))# x=int(input()) it stores integer while x= print(int(input())) it stores none
y_co_ordinate=int(input("y="))
tup=(X_co_ordinate,y_co_ordinate)
distance=((tup[0]**2)+(tup[1]**2))**0.5
print(distance)
# set
# set()=empty set
s={1,2,2,3} # set ignore the duplicate value while printing and it's gives unordered collection of data
print(s)
print(type(s))
print(len(s))
A={4,5,6,9,8}
B={3,4,2,0,6}
print(A|B)# print(A.union(B)) as same as print(A|B)
print(A&B) # print(A.intersection(B)) as same as print(A&B)
print(A-B)
print(A^B) # it eliminates the same element in both the set and then provide A&B in one sets.
print(A.add(3))
print(A)
print(A.remove(4))
print(A)
A.clear()
print(len(A))
print(A.pop)  
# dictionary
# # dictionary 
dict={"name":"zabihllah",  "course":"CSE","class":13 }# here dict is assighner (it can be any thing),here name ,cse,class, are key value of the dictionary
print(dict)
print(dict["course"])#it will give us error as output when we take invalid input.
print(dict.get("course")) # it will give us none output when we take invalid input.
print(dict.keys())
# nesting in dictionary 
my_dict={"name":"salim", "course":"cse","marks":{"maths":"75","physics":"85","chemistry":92,},  "climate":("weather","hot","cold")}
print(my_dict["marks"])
# dictionary method
print(my_dict.keys())
print(my_dict["marks"]["physics"])
print(len(my_dict)) # we use this syntax to find length of any data.
# type casting can be use in any type of  data or function.
print(list(my_dict.keys())) 
print(len(list(my_dict.keys())))
print(my_dict.values())
print(my_dict.items())
print(list(my_dict.items()))
pairs=(list(my_dict.items()))
print(pairs)
my_dict["city"]="new delhi"# same as 68
print(my_dict)
(my_dict.update({"city":"new delhi"}))
print(my_dict)'''
A="hello"
print(A[4]) # here we can clearly see the consecutive same letter count as one index no.
print(len(A)) # don't get confuse here finding no. of character it is counting all character whether the letters are consecutive or not.
# unification 
print(chr(65))
print(ord("A"))
# type conversion 
print(bin(13))
#slicing of binary & oct & hex
print(bin(13)[2:])
y=int(input("enterd a integer:"))
print(hex(y))
print(hex(y)[2:])
print(bin(y))
print(oct(y))
print(oct(y)[2:])
print(complex(y,0))
# print(eval)
a=1
b=5
print(eval("a+b"))
print(type(eval("a+b")))


                  
