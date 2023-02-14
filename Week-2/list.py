names = ['Asta','Leon','Zoro','Sanji','Itachi']

#Accessing items in a list
print(names)
print(names[0])
print(names[2])
print(names[-1])
print(names[0:3])

#list of fruits
fruits = ["Mangoes","Apples","Guavas","Orange","Avocado","melon","lime"]
print(fruits)
print(fruits[0:-1])
print(fruits[3])

#print
print("My favourite fruit is ",fruits[4].upper())

#Adding two lists
vegetables = ["kales","cabbage","spinnach","managu","carrots","brocoli"]
stationary = ["pens","ink","paper","glue","scissors","stapler"]

shoppings = vegetables + stationary
print(shoppings)
print(shoppings[5])

#for loop
for vegetable in vegetables:
    print(vegetable)

for shopping in shoppings:
    print(shopping)

print("My name is " + names[1] + " and my favourite fruit is " + fruits[3])