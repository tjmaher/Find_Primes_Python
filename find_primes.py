#   Thomas F. Maher, Jr. ("T.J.")
#   tj.maher@gmail.com 
#  	Senior QA Lead / BSCS / Masters of Software Engineering

#   Assignment: Write an efficient, well documented program in the language 
#   of your choice that will return the first n prime numbers.
#
#   This assignment was written in Python 2


from sys import argv

def getInputNumber():
	""""
	This function, when called: 
	1) Print out a question to the user asking how many prime numbers need to be found.
	2) Gets the input from the user. 
	3) Checks if the input was in the form of an integer. If not (such as "#, $, %) a ValueError is thrown, executing
	   the "except" statement, printing out the "txtInvalidEntry" message, looping back to the query on how many prime numbers to find. 
	4) If the input value is less than or equal to zero (such as -1, 0) it prints out the "txtInvalidEntry" message, 
  	   looping back to the query on how many prime numbers to find. 
 	5) If it passes these conditions in the "try" block, it returns the sanitized input to the main program.  
    # Prompt, txtInvalidEntry: These variables store "constants" that are used
	# to format output text to the user. They are stored in the variables and
	# not in the body of the code for readability. 
	"""
	prompt = '> '
	txtInvalidEntry = "\n*** INVALID ENTRY: ****\n*** Please enter input in the form of a positive integer.\n" 

	while True:
		print "*** How many prime numbers would you like me to find?"
		try:
			userInput = int(raw_input(prompt)) 	# Get user input and attempt to format it to be an integer. 
			if userInput <= 0:					# We are looking for only positive integers, greater than zero.
				print txtInvalidEntry			# If it is less than or equal to zero, print txtInvalidEntry
			elif userInput > 0:					# If the integer is positive, we will use that value.
				return userInput				# Return the value of the userInput to the main program
		except ValueError:						# If the raw_input could not be formatted to be an integer, a ValueError is thrown. 			
				print txtInvalidEntry			
				
def isPrime(intTestNumber):
	"""
	isPRIME: Function is based off of http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes ... 
		Input: an integer n > 1
		Let A be an array of Boolean values, indexed by integers 2 to n, initially all set to true.
			for i = 2, 3, 4, ..., not exceeding (Square root of) n:
				if A[i] is true:
					for j = i2, i2+i, i2+2i, ..., not exceeding n:
						A[j] := false
			Output: all i such that A[i] is true.
	"""
	
    if intTestNumber == 2:					# "intTestNumber" is the number we are testing if it is prime or not. 
        return True							# If the number being tested is 2, then, yes, 2 is a prime number. Return that it is a prime number. 
    elif intTestNumber < 2 or not intTestNumber % 2: # If the number is less than 2, or is an even number (divisible by 2), it is not prime. 
        return False
    for i in range(3, int(intTestNumber ** .5 + 1), 2): # Sieve of Eratosthenes: Search from 3, 5, 7 ... up until the Square root of the number. 
        if not intTestNumber % i: return False			# Is the test number divisible of 3, 5, 7, or whatever, it is not a prime number. 
    return True											# If it passes all these tests, return that the number is actually prime. 
	
def findPrimes(intMaximumNumberPrimes):
	arrayOfPrimes = [2,]	# Initialize the array set with the first prime number: [2]. 
	intCountOfPrimes = 1	# Since we cheated and added the first number to the array: Initialize count to "1". 
	testNum = 3 			# Since we hardcoded the first value, 2, in the array, the next number to test is "3". 

	while intCountOfPrimes < intMaximumNumberPrimes:# Do while the number of primes found is less than the user's input value 
		if isPrime(testNum):						# Call up the function "isPRIME", submitting the number we need to test. 
			arrayOfPrimes.append(testNum)			# If function returns "True", and the number is prime, we are going to add the number to the array. 
			intCountOfPrimes += 1					# If the function is "True", increment the intCountOfPrimes by one. 
		testNum += 2								# To save time, we are going to skip to the next odd number, testing out first 3, 5, 7, 9 (etc) 
	print "\nSet of Prime Numbers: %r\n" % (arrayOfPrimes) 	# Once we reach the maximum number of primes we were told to find, we print out the array. 


while True: 
	print """
	*** FIND_PRIMES_TMAHER returns the first N primes. ***
	*** Select CTRL-C to end the program.              ***
	"""

	maxNumPrimes = getInputNumber()						# Ask the user how many primes to find. Call the function getInputNumber and store value in maxNumPrimes.				
	print "\n*** Attempting to find the first %i prime numbers..."	% (maxNumPrimes)		
	findPrimes(maxNumPrimes)							# Call the function that will find the maximum number of primes. 
