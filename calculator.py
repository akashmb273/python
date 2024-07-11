#completed
import os
def add(a,b):
    c= a+b
    print(f"Sum of 2 numbers is {c}")
    return c
def sub(a,b):
    c= a-b
    print(f"Difference of 2 numbers is {c}")
    return c
def mul(a,b):
    c= a*b
    print(f"Multiplication of 2 numbers is {c}")
    return c
def div(a,b):
    c= a/b
    print(f"Division of 2 numbers is {c}")
    return c

op_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def fun():
    a = int(input("Enter the First number :  "))
    print('''Choose an Operation  :
    +
    -
    *
    /
    ''')
    temp = True
    while temp:
        op = input("Enter the operation :  ")
        b = int(input("Enter the Second number :  "))
        cal_fun=op_dict[op]
        out=cal_fun(a,b)
        print(f"Do You want to continue with {out} (y) or Start a new Operation(n) or exit(x)")
        ch=input("Choice (y/n/x)  :  ").lower()
        if ch=="y":
            a=out
        elif ch=="n":
            temp=False
            os.system('cls')
            fun()
        elif ch=="x":
            break


fun()
