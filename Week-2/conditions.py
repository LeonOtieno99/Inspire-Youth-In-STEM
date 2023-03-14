#compound/multiple conditions

age= 18
gender = "male"

if(age>30) & (gender == 'male'):
	print("Your qualify for a loan")
else:
	print("No loan for you")

fav_color = "grey"
age = 22
if (fav_color == 'grey') | (age <= 20):
	print("Happy birthday to you")
else:
	print("No birthday present for")
