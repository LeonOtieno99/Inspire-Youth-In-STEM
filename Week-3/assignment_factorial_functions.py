#write a program to calculate factorial of a number using functions
def factorial(n):
    if n < 0:
        print("No factorial for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))

#write a program to calculate simple interest
def simple_interest(P,R,T):

    simple_interest = ((P)*(R)*(T/12))/100
    print(simple_interest)

principle = int(input("Enter the principle amount: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time: "))

simple_interest(principle,rate,time)