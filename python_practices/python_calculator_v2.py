def display_menu():
    print("\n===Calculator Menu===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

def get_choice():
    while True:
        try:
            ch=int(input("Choose 1-6 : "))
            if ch<1 or ch>6:
                raise ValueError
            break
        except ValueError:
            print("Invalid Input! Kindly reselect ")
    return ch

def get_numbers():
    while True:
        try:
            num1=float(input("Enter first number :"))
            num2=float(input("Enter second number :"))
            return num1,num2
        except ValueError:
            print("wrong input! Enter numbers only...")
    
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("Division by 0 not possible!")
    else:
        return a/b
    
def mod(a,b):
    if b==0:
        print("Mod by 0 not possible!")
    else:
        return a%b
    
def main():
    while True:
        display_menu()
        choice=get_choice()

        if choice==6:
            print("Exiting Calculator...!")
            break

        num1,num2=get_numbers()
        
        if choice==1:
            result=add(num1,num2)
            print(num1,"+",num2,"=",result)
        elif choice==2:
            result=subtract(num1,num2)
            print(num1,"-",num2,"=",result)
        elif choice==3:
            result=multiply(num1,num2)
            print(num1,"x",num2,"=",result)
        elif choice==4:
            result=divide(num1,num2)
            if result is not None:
                print(num1,"/",num2,"=",result)
        elif choice==5:
            result=mod(num1,num2)
            if result is not None:
                print(num1,"%",num2,"=",result)

if __name__ == "__main__":
    main()

    