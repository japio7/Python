
def distance(lst):
	"""
	Displays the distance of coordinate points.

	Args:
		lst (list): A list of tuples.

	Returns:
		tuple: A tuple of two points with the lowest distance.
	"""
	minDist = float("inf")
	for i in range(0, len(lst)):
		for k in range(i+1, len(lst)):
			x1, y1 = lst[i]
			x2, y2 = lst[k]
			dist = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)
	return dist

lstTups = [(1, 4), (5, 3)]

print(distance(lstTups))
