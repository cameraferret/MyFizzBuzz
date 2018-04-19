#Fizz Buzz
#Randolph Wilson
#This basic script should perform the fizz buzz task.

for i in range(100):
	if(i % 3 == 0 and i % 5 == 0):
		print("Fizz Buzz")
	elif(i%3 == 0):
		print("Fizz")
	elif(i%5 == 0):
		print("Buzz")
	else:
		print(i)