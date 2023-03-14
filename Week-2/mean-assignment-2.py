#find average of first 10 numbers from user input

numbers = []
sum_num = 0


print("Enter first 10 numbers")
for number in range(0, 10):
    num = int(input("Input number: "))
    numbers.append(num)
    sum_num = sum_num + numbers[number]

print("Total of the list: ",sum_num)
avg_num = sum_num / len(numbers)
print("Average of list: ",avg_num)