
def distance(lst):
	"""
	Displays the distance of coordinate points.

	Args:
		lst (list): A list of tuples.

	Returns:
		float: The distance between two points.
	"""
	for i in range(0, len(lst)):
		for k in range(i+1, len(lst)):
			x1, y1 = lst[i]
			x2, y2 = lst[k]
			dist = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)
	return dist

lstTups = [(1, 4), (5, 3)]

print(distance(lstTups))
