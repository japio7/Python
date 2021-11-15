array = [14, 28, 19, 15, 20, 33, 3, 17, 10]

def createHashTab(lst):
	table = [[] for x in range(len(lst))]
	for i in lst:
		a = i%len(lst)
		table[a].append(i)
	return table

def findValueHash(lst, val):
	index1, index2 = 0, 0
	foundNumber = False
	for ls in lst:
		if val in ls:
			index1 = lst.index(ls)
			index2 = lst[index1].index(val)
			foundNumber = True
	if not foundNumber:
		return f"{val} not in list!"
		
	return f"{val} found at index {index1,index2}"

print(createHashTab(array))
print(findValueHash(createHashTab(array), 10))