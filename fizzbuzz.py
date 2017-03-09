"""function that checks the divisibility of 3, 5 or both"""
"""a number divisible by both 3 and 5 id a divisor 15, divisibility rule"""
def fizz_buzz(num):
	if num%15==0:
		return "FizzBuzz"
	elif num%5==0:
		return "Buzz"
	elif (num%3==0):
		return "Fizz"
	else:
		return num

