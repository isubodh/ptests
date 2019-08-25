import sys

def isPrime(num):
	if num < 0 :
		return False
	if (num < 3):
		return  True
	factor = 2
	while factor < num:
		if num % factor == 0:
			return False
		else:
			factor += 1

	return True
	
def isEven(num):
	if num % 2 == 0:
		return True
	else:
		return False
		

def isOdd(num):
	if num % 2 == 1:
		return True
	else:
		return False		

if __name__ == "__main__":
	num = int(sys.argv[1])
	print("Prime :", isPrime(num))
	print("Even :", isEven(num))
	print("Odd :", isOdd(num))