from models_ import Point


def calculate_area(
		points:list[Point]
		)->float:
	"""Recibe una lista de puntos y retorna el area formada por los coordenadas de cada punto"""
	sumatory1 = 0
	sumatory2 = 0
	for i in range(len(points)-1):
		print(points[i+1].north)
		print(points[i].north)
		sumatory1 += (points[i].east * points[i+1].north)
		sumatory2 += (points[i].north * points[i+1].east)
	
	return (sumatory1-sumatory2)/2

