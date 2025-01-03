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