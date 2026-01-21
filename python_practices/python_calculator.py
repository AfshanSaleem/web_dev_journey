print("Calculator Options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder(Mod)")

while True:
    try:
        choice=int(input("Select 1-5:"))
        if(choice<1 or choice>5):
            raise ValueError
        break
    except ValueError:
        print("Enter a valid number!")

#Calculator logic
while True:
    try:
        num1=int(input("Enter first number :"))
        num2=int(input("Enter second number :"))
        break
    except ValueError:
        print("wrong input! Enter integers only...")
if choice==1:
    print(num1,"+",num2,"=",num1+num2)
elif choice==2:
    print(num1,"-",num2,"=",num1-num2)
elif choice==3:
    print(num1,"x",num2,"=",num1*num2)
elif choice==4:
    if num2==0:
        print("Division by 0 not possible")
    else:
        print(num1,"/",num2,"=",num1/num2)
elif choice==5:
    if num2==0:
        print("Remainder by 0 not possible")
    else:
        print(num1,"%",num2,"=",num1%num2)