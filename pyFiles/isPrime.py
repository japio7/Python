def isPrime(p):
	if p == 2:
		return True
	if p%2 == 0 or p < 2:
		return False
	for n in range(3, p//2, 2):
		if p % n == 0:
			return False
	return True

print(isPrime(13))
