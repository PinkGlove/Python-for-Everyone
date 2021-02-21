largest = None
smallest = None
while True:
	try:
		num = input("Enter a number: ")
		if num == "done":
			print("Maximum is", largest)
			print("Minimum is", smallest)
			break
		number = int(num)
		if (largest is None) & (smallest is None):
			largest = number
			smallest = number
		else:
			if largest < number:
				largest = number
			if smallest > number:
				smallest = number
	except:
		print("Invalid input")
		continue
