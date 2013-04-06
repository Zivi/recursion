def to str(n,base):
	#set up key
	convert_string = "0123456789ABCDEF"
	#check if the input number is less than the base
	if n < base:
		#return the number, no need to operate to find it in base
		return convert_string[n]
	else:
		#call the function again, append the last digit of the number