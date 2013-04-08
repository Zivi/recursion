def to str(n,base):
	#set up key
	convert_string = "0123456789ABCDEF"
	#check if the input number is less than the base
	if n < base:
		#return the number, no need to operate to find it in base
		return convert_string[n]
	else:
		#call the function again, append the last digit of the number
		return toStr(n/base,base) + convert_string[n%base]

def listsum(num):
	#intialize the adder
	sum = 0

	# Initialize numList
	numList = str(num)
	# #iterate through each item in the number list
	# #the sum is equal to the previous some plus the next
	# #item in the list
	for charNum in numList:
		sum += int(charNum)
	#check if sum is only one digit, if it's still 10 or
	#more, add the digits together
	if sum <= 9:
		return sum 
	else:
		return listsum(sum)

num1 = 415894671
print "The checksum for %d is: %d" % (415894671, listsum(415894671))
