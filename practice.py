# print("avi"+" "+"jain"+str(4))
# print(4+int(10.234))
# print(5>10)
# print(type(False))

# name = input()
# print("Your Name is: ",name)

# x=y=z=t=50
# print(type(z))

# name,age,attractive = "Avi",24,True
# print(name)
# print(age)
# print(attractive)

# name = "AviJain"
# print(len(name))
# print(name.lower())
# print(name.upper())
# print(name*3)
# print(name.capitalize())
# print(name[0::3])
# first_name = name[0:2:-1]
# print(first_name)

# i=0
# while i<=100:
#     print("You are Stupid")
#     i += 1

# name=""
# while len(name)==0:
#     name = input("Enter Your Name: ")
# print("Hello "+name) 

##For Loop:
# import time
# for i in range (10,0,-1):
#     print(i)
#     time.sleep(1)
# print("Yayy")

# for i in "Avi Jain":
#     print(i)

##Nested Loops

# for i in range(5):
#     for j in range(x,y):
#         print("*",end="")
#     print("*")
# print("Rectangle")
# for i in range(5,0,-2):
#     print("*"*5)

# while True:
#     name = input("What is your name? ")
#     if name != "":
#         break

# for i in range(10):
#     if i == 5:
#         pass
#     else: print(i)
    
# name = ["avi","jain","random"]
# print(name[3])

# for i in name:
#     print(i,end=" ")
# name.insert(1,"noni")
# print(name)
# name.clear()
# print(name)
# name.append("noni")
# print(name)


# name = ["avi","ruchi","dimpy"]

# # for x in name:
# #     print(x)
# classes = [5,8,10]
# subject = ["maths","english","science"]

# list = []
# list.append(classes)
# print(list)
# school = [name,classes,subject]

# # print(school[0][2])

# for i in range(10):
#     if i == 5:
#         continue    
#     print(i)


# for y in range(3):
#     for x in range(3):
#         print(school[x][y],end=" ")
#     print()

# print(school[1][0])

# random_list = ["avi","2","true","enterprenuer"]
# new_list = random_list[0]
# print(random_list)
# print(new_list)
# new_list.insert(2,"apple")
# print(new_list)
# print(random_list)

# avi = [random_list,new_list]
# print(avi)


# student = ("bro",21,"male")
# for x in student:
#     print(type(x))
# print(len(student)) 

# student.index(21)

utensils_list = ["fork","spoon","knife","knife"]
utensils_tuple = ("fork","spoon","knife","knife")
utensils_set = {"fork","spoon","knife","knife"}
utensils_list.index("knife")
utensils_list[0]
utensils_tuple[0]
utensils_set[0]

# for x in utensils_list:
#     print(x)
# for x in utensils_tuple:
#     print(x)
# for x in utensils_set:
#     print(x)

##Dictionaries:
capitals = {'USA':'WDC','India':'Delhi'} 
print (capitals.get('India'))

print(capitals.get('Germany'))
# print(capitals.get('India'))
print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
print(capitals)

# for key,values in capitals.items():
#     print(key,values)
    


# def random(name,last_name,age):
#     print("Hello",name,last_name)
#     print("Your age is:",age)

# a= "Avi"
# b = "Jain"
# c= 22
# random(a,b,c)

# def multiply(a,b):
#     return a*b

# x= multiply(8,9)
# x

# def random(a,b,c):
#     print("Hello",a,b,c)
# random(c="type",b="jain",a="avi")


# def fxn(*a):
#     b=0
#     for i in range(5):
#         a=i*i
#         b=b+a
#     return b

# fxn(1,2,3)
# b=0
# for i in range(1,5):
#         a=i*i
#         b=b+a
#         print (a,b)

# d=0
# 


# def radnom(b,c):
#     print("Hello")
#     return b*c,b+c,b-c,round(b/c,2),b%c,"Hello"
# def fxn(*a,b):
#      d=0
#      for i in a:
#         c=i*i
#         d = d+c
#      return d,b       

# fxn(1,2,3)
# radnom(5,7)

# def test(a):
#     print(a)
# test("Avi")

# def random(a,b):
#     return a*b

# print("input a string")
# z=input()
# print("My Name is",z,"and i will perform multiplication today!")
# print("Can you give me two numbers!!")
# x=int(input())
# y=int(input())
# print("Your result is",str(random(x,y)))

# a= 0
# b=1
# list=[0,1]
# n = int(input())
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
#     list.append(c)

# print(list)

# new = [1,2,3,4,5]
# new="Avi Jain"
# new[0],new[4]=new[4],new[0]
# temp=[]
# x=len(new)
# print(x)
# for i in range(x):
#     a=new[x-1-i]
#     temp.insert(i,a)
#     print(i)
# print(temp)

# tup = (1,2,3,4,5,5)
# tup[2]=4
# tup[6]=3
# print(tup)

# lis = [1,2,3,4,5]
# lis[2]=6
# lis.insert(0,2)
# print(lis)
# lis.pop()    
# # lis = [1,2,3,4,5]
# # tup = [1,2,3,4,5]
# sets = {1,2,3,4,4,34,343,4,34,3,4,3,43,4,3,43434,54,55,6,4,4,2}
# print(sets)
dic = {1:"Avi",2:"Jain",3:"Me",4:"random",1:"type"}
print(dic)
dic[5]
print(dic.get(5))
dic.values()

for keys,values in dic.items():
    print (keys,'')
for i in range(5):
    print(i,end=" ")
# def random(*a,b):
#     c=0
#     for i in a:
#         c=c+i*i
#     return c+b

# random(1,2,3,4,5,b=45)

# print("My name is {} and my age is {}".format("Avi",21))
# print("My name is {1} and my age is {0}".format("Avi",21))
# print("My name is {name} and my age is {age}".format(name="Avi",age=21))
# text = "My name is {} and my age is {:E}"
# different types of notations
# {:.2f},{:,},{:b},{:X},{:E}
# text.format("Avi",2122323)

# import random
# x= random.randint(1,6)
# y =random.random()
# print(x,y)
mylist = ["avi","vishu","kurmi"]
new = []
for i in range(100000):
    a= random.choice(mylist)
    new.append(a)

new.count("avi")
new.count("vishu")
new.count("kurmi")

# random.shuffle(mylist)
# print(mylist)

# x= lambda a,b,c:a+b+c

# def random(a):
#     return lambda x: a*x+a+x

# t = random(2)
# t(4)

# import datetime
# new = ['avi',"vishu","kurmi"]
# random.choice(new)

# print(dir(datetime))

# from datetime import datetime
# import time
# while 1==1:
#     print(datetime.now())
#     time.sleep(1)


# name = input("Enter your name: ")
# age = input("Enter your age:  ")

# text = "Your Name is {} and your Age is {}"
# print(text.format(name,age))

# try:
#     num1 = int(input("enter a number: "))
#     num2 = int(input("enter a number: "))
#     result = num1/num2
#     print(result)
# except Exception:
#     print("there was an error")

# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# result = num1/num2
# print(result)

# 55/0
# 55/avi


# import random
# print(dir(random))
def rand(i):
    list = []
    for x in range(1,i+1):
        list.append(x)
    return list

rand(10)

a= rand(5)
print(a)
import random
random.choice(a)
print(dir(random))
random.randint(1,100)
