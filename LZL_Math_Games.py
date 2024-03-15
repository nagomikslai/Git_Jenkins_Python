print("")
print("This is a Fun Math Game!", "\n")

while True: 
    print("============")
    print("If x + y = 5")
    print("If x - y = 1")
    print("============")
    print("\n")
    x=input("What number is x ")
    a=int(x)
    y=input("What number is y ")
    b=int(y)
    print("\n")

    if a+b == 5 and a-b == 1:
        print("Yes! Your answer is CORRECT!!!")
        print(x, "+", y)
        print(a+b)
        print("This is Addition")
        print("\n")
        print(x, "-", y)
        print(a-b)
        print("This is Substraction")
        print("\n")
    else:
        print("Wrong Answer!!!")
        print("Try Again...")
        print("\n")
    
