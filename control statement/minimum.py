num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if(num1<num2)and(num1<num3):
 print("minimum nuber is ",num1)
elif(num2<num3)and(num2<num1):
 print("minimum number is ",num2)
elif(num3<num1)and(num3<num2) :
 print("minimum number is ",num3)
else: ("all number are equal",num1,num2,num3) 

