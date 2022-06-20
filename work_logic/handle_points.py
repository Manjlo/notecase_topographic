from cmath import sqrt, atan
from math import pi
from models_.main import Point, Side


def calculate_diferences(
		point1:Point,
	 	point2:Point
	 	)->list[float]:

	"""recibe dos puntos, el primero se toma como punto donde esta,
	 el segundo como punto hacia donde va, retorna la diferencias 
	 en este y norte teniendo en cuenta el orden"""

	north_diference = (point2.north - point1.north)
	east_diference = (point2.east - point1.east)

	return [north_diference, east_diference]

def calculate_distance(
		points:list[Point]
		)->float:

	"""recibe una lista de 2 puntos y retorna la distancia entre ellos"""

	[y_diference, x_diference] = calculate_diferences(points[0], points[1])
	distance = sqrt(y_diference**2 + x_diference**2)
	return round(distance.real, 2)

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
	course_angle = abs(atan(x_diference/y_diference)*180/pi)
	azimut_value = definite_azimut(y_diference, x_diference, course_angle)

	return round(azimut_value.real, 3)

def definite_side_name(
		points:list[Point]
		)->str:
	"""Recibe una lista de puntos y calcula su nombre apartir de ahi"""

	return f'{points[0].name} to {points[1].name}'

def handle_side(
		points:list[Point]
		)->Side:

	"""Recibe una lista de 2 puntos, retorna el azimut 
	y la distancia en el orden en que se reciben los puntos"""

	return Side(
		name = definite_side_name(points),
		azimut   = calculate_azimut(points),
		distance = calculate_distance(points)
		)
	





	

