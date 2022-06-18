from math import sin, asin, pi
from models.main import Side
from work_logic.handle_points import handle_side


def definite_inter_angle(
		az1:float, 
		az2:float
		)-> float:
	
	"""Recibe dos angulos azimutales que delimitan un punto 
	para encontrar el angulo interno de ese punto"""

	if az1 > az2:
		return az1-az2
	elif az1 == az2:
		raise ValueError("Se esperan dos azimuts diferentes, no iguales")
	else: 
		return az2-az1
	

def calculate_angular_error(
		**kargs
		)->float:
	"""Recibe 3 puntos de cierre el 1, el 4 y 1 prima, y retorna el error angular"""
	point1 = kargs.get('p1')
	point1_p = kargs.get('p1_prime')
	point4 = kargs.get('p4')

	p1_to_p4   : Side = handle_side([point1, point4])
	p1_to_p1_p : Side = handle_side([point1, point1_p])
	 
	angle_p1 = definite_inter_angle(p1_to_p4.azimut, p1_to_p1_p.azimut)

	#se utiliza la ley de senos para encontrar 
	# el angulo que forma el punto 4 con el punto 1 y  punto 1 prima
	
	angle_error = asin((p1_to_p1_p.distance * sin(angle_p1*pi/180))/ p1_to_p4.distance)
	return angle_error











