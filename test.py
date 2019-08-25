import mymath 

def test_isPrime():
	assert mymath.isPrime(-1) == False, "-1 Prime Undefined"
	assert mymath.isPrime(0) == True, "0 is Prime"
	assert mymath.isPrime(1) == True, "1 is Prime"
	assert mymath.isPrime(2) == True, "2 is Prime"
	assert mymath.isPrime(3) == True, "3 is Prime"
	assert mymath.isPrime(5) == True, "5 is Prime"
	assert mymath.isPrime(6) == False, "6 is not Prime"
	assert mymath.isPrime(20) == False, "20 is not Prime"
	assert mymath.isPrime(23) == True, "23 is Prime"
	
def test_isEven():
	assert mymath.isEven(0) == True
	assert mymath.isEven(2) == True
	assert mymath.isEven(10) == True
	assert mymath.isEven(200) == True
	assert mymath.isEven(1) == False
	assert mymath.isEven(3) == False
	assert mymath.isEven(99) == False
	assert mymath.isEven(199) == False	
	
def test_isOdd():
	assert mymath.isOdd(0) == False
	assert mymath.isOdd(2) == False
	assert mymath.isOdd(10) == False
	assert mymath.isOdd(200) == False
	assert mymath.isOdd(1) == True
	assert mymath.isOdd(3) == True
	assert mymath.isOdd(99) == True
	assert mymath.isOdd(199) == True
	
if __name__ == "__main__":
	test_isPrime()
	print("isPrime PASSED")
	test_isEven()
	print("isEven PASSED")
	test_isOdd()
	print("isOdd PASSED")
	print("--- Everything passed ---")