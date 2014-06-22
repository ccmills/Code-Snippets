## FizzBuzz is a deceptively tricky little challenge: Print all the integers from 1 to 100, and for
## numbers that are multiples of 3, print "Fizz" next to them. For numbers that are integers of 5,
## brint "Buzz". For both, print "FizzBuzz". There are solutions using 3 tests (one for 3, one for
## 5, and one for 3*5), but by concatenating strings, here's a way to do it with only two tests.

i = 1 # index counter
a = 0 # multiple of 3 test variable
b = 0 # multiple of 5 test variable

#run loop 100 times; i incremented at end of loop:
while i < 10001:
	#store index as string (and space for formatting)
	c = str(i) + ' '
	#test for multiple of 3 using only integer math. Since i/3 will return a
	#particular integer for the first time when it's a multiple of 3, we use 'a' to 
	#test if we've seen the value of i/3 before. If we have, it's not a multiple of 3,
	#if not, it is. i/3>0 lets us ignore numbers less than the first multiple. 
 	if i/3 > 0 and i/3 !=a:
 		#add "Fizz to the string"
		c +='Fizz'
		#store the value of i/3 so we ignore numbers until the next multiple
		a = i/3
	#also test if multiple of 5. Since we're building onto the string "c", there's no need for a
	#third check. If a number is a multiple of 3 it will have already had "Fizz" concatenated in the
	#prior test. If not, it will have passed through.
	if i/5 > 0 and i/5 !=b:
		c +='Buzz'
		b=i/5
	#Print final string c, which will be i if not a multple of 3 or 5, i + Fizz if a multple of 3
	#i + Buzz if a multiple of 5, and i + FizzBuzz if a multiple of both 3 and 5
	print c
	i += 1