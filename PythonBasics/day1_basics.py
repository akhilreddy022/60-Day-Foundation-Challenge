#swapping of  two numbers
a=10
b=5
print("before swap",a,b)
temp=a
a=b
b=temp
print("after swap",a,b)


#addition of two numbers
a=10
b=20
c=a+b
print("the addition of two numbers is:",c)

#user input addition
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print("sum=",a+b)


#celsius to fahrenheit
c=int(input("celsius is:"))
f=(c*9/5)+32
print("conversion of celsius to fahrenheit is =",f)


#simple interest
p=float(input("enter principle:"))
r=float(input("enter rate:"))
t=float(input("enter time:"))
SI=(p*r*t)/100
print("the simple interest is =",SI)

#area of circle
r=float(input("enter radius:"))
area=3.14*r*r
print("the area of circle is =",area)

#area using mathpi
import math
r=float(input("radius is:"))
area=math.pi*r*r
print("area of circle is =",area)

#area of rectangle
l=float(input("enter length:"))
b=float(input("enter breadth:"))
area=l*b
print("the area of rectangle is =",area)

#total minutes converter
ttime=float(input("enter total time:"))
hours=ttime//60
minutes=ttime%60
print(f"{ttime} minutes = {hours} hours and {minutes} minutes")

#bmi calculator
w=float(input("enter weight in kg:"))
h=float(input("enter height in M:")) #height in meters
BMI=w/(h)**2 #bmi=weight/(height*height)
print("bmi=",BMI)

#find remainder
a=int(input("enter a:"))
b=int(input("enter b:"))
print("remainder=",a%b)

#name and age as a sentence
name=str(input("enter name:"))
age=int(input("enter age:"))
print("the person's name is",name,"and age is", age)
