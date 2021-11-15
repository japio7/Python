import random

def passwordGenerator():
	letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
		'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
	uppers = [x.upper() for x in letters] 
	numbers = ['0','1','2','3','4','5','6','7','8','9']
	chars = letters + uppers + numbers

	pw = ""
	for i in range(6):
		pw += random.choice(chars)
	pw += "-"
	for i in range(6):
		pw += random.choice(chars)
	pw += "-"
	for i in range(6):
		pw += random.choice(chars)
	return pw

print(passwordGenerator())

