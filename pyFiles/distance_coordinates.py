def distance(p1, p2):
	"""
	Displays the distance of two coordinate points.

	Args:
		p1 (float/int): Coordinate Point 1.
		p2 (float/int): Coordinate Point 2. 

	Returns:
		float: The distance between two points.
	"""
	for i in range(2):
		for k in range(i+1, 2):
			x1, y1 = float(p1[0]), float(p1[1])
			x2, y2 = float(p2[0]), float(p2[1])
			dist = (((x2 - x1)**2) + (y2 - y1)**2)**(1/2)
	return (dist)

print(distance((1, 4), (5, 3)))