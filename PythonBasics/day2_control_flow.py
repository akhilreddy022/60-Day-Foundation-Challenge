#positive/negative
num=int(input("enter a number:"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("zero")


#greatest of three
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))  

if a>=b and a>=c:
    print("a is greatest",a)
elif b>=a and b>=c:
    print("b is greatest",b)
else:
    print("c is greatest",c)

#grade calculator
num=int(input("enter marks:"))
if num>=90:
    print("a grade", num)
elif num>=80:
    print("b grade",num)
elif num>=70:
    print("c grade",num)
else:
    print("d grade",num)

#even or odd
num=int(input("enter a number:"))

if num%2 == 0:
    print("even")
else:
    print("odd")

#sum of 1 to 100
total=0
for i in range(1,101):
    total += i
print("sum=",total)

#multiplication table
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#count digits
n = int(input("Enter number: "))
count = 0

temp = n  # copy

while temp > 0:
    temp = temp // 10
    count += 1

print("Digits:", count)

#reverse a number
n = int(input("Enter number: "))
rev = 0
temp = n

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reversed =", rev)

#factorial
n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
