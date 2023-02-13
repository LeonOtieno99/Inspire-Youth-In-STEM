#write a program to calculate simple interest

P = input("Enter the principle amount: ")
R = input("Enter the rate: ")
T = input("Enter the time: ")

simple_interest = (int(P)*int(R)*int(T))/100

print(simple_interest)