print("Hello,Welcome to Python!")
print("Harohalli")
print("Kanakapura Road")
L1=[1,2,3,4,5]   #lists
print(type(L1))
#sets 
s1={1,2,3,4,5}
print(type(s1))
#tuple
s1=(1,2,3,4,5)
print(type(s1))
#complex
a=2+3j
print(type(a))
#getting keywords of python language
import keyword
print("keywords of python are:",keyword.kwlist)
b=56
print("type of value in b is:",type(b)) #knowing the type of value assigned to the variable 'b'
print("b:",b)  #printing the value stored inside the variable 'b'
c=2.0
print("type of value in c is:",type(c))
print("c:",c)
d=2+4j
print("type of value in d is:",type(d))
print("d:",(d))
name=input("What is your name ?:")
print("Helloo!!",name,"!")
#printing output as per age condition for below 18,18,and above 18
age=int(input("Enter you age:"))
if age<18:
    print("You are a kid")
elif age==18:
    print("You are an adult now!")
else:
    print("You are above 18.")
    print("hello lets start our assignment")
x=28
print(x)
y=22
print("y:",y)
print(x+y)
print("Rahul","emma","priti",25,35,56,23.87,98.06,98.04,sep=" , ")
print("Rahul","emma","priti",25,35,56,23.87,98.06,98.04, sep="\n")
print("Rahul",26 ,end=" ")
print("emma", 27, sep="\n")
# expression-> x+y where x and y are operands and + is operator or arithmetic
a=5
b=7
print(a,b)
print(a//b)
print(-3//2)
#in floor division it is floored to nearest integer 
print(a,b)
print(a*b)
print(a**b)
print(a%b)
''' comparision operators are as == checks equality,<= checks smaller and  equal,>= checks greater and equal,!= checks wwhether not equal to'''
a=6
b=3
print(a==b)
print(3==3)
print (a!=b)
print(3!=3)
print(a>b)
print(b>a)
print(6>=3)
print(3<=6)
print(3>=3)
print(2>=3)
