from cmath import sqrt, atan
from math import pi
from models.main import Point, Side


def calculate_diferences(
		point1:Point,
	 	point2:Point
	 	)->list[float, float]:

	"""recibe dos puntos, el primero se toma como punto donde esta,
	 el segundo como punto hacia donde va, retorna la diferencias 
	 en este y norte teniendo en cuenta el orden"""

	north_diference = (point2.north - point1.north)
	east_diference = (point2.east - point1.east)

	return north_diference, east_diference

def calculate_distance(
		points:list[Point]
		)->float:

	"""recibe una lista de 2 puntos y retorna la distancia entre ellos"""

	coordinates_diference = [calculate_diferences(points[1], points[2])]
	distance = sqrt(coordinates_diference[0]**2 + coordinates_diference[1]**2)
	return distance

def definite_azimut(
		diference_north:float, 
		diference_east:float, 
		course_angle:float
		)->float:

	"""recibe las diferencias de las coordenadas 
	para a partir de rumbos calcular el verdadero angulo azimut"""
	if diference_east > 0 and diference_north > 0:
		return course_angle
	if diference_east > 0 and diference_north < 0:
		return 180-course_angle
	if diference_east < 0 and diference_north < 0:
		return course_angle + 180
	if diference_east < 0 and diference_north > 0:
		return 360-course_angle
 
def calculate_azimut(
		points:list[Point]
		)->float:

	"""recibe una lista de 2 puntos el primero debe de ser el punto donde esta,
	 el segundo punto es hacia donde va el azimut y retorna el azimut"""

	[y_diference, x_diference] = calculate_diferences(points[0], points[1])
	course_angle = atan(x_diference/y_diference)*180/pi
	azimut_value = definite_azimut(y_diference, x_diference, course_angle)

	return azimut_value

def handle_side(
		points:list[Point]
		)->Side:

	"""Recibe una lista de 2 puntos, retorna el azimut 
	y la distancia en el orden en que se reciben los puntos"""

	return Side(
		points=points,
		azimut =calculate_azimut(points),
		distance = calculate_distance(points)
		)
	





	

