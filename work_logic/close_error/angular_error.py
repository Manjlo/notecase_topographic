from models_.main import Point
from work_logic.handle_points import calculate_azimut, handle_side

def definite_inter_angle(angle:float)->float:
	"""Recibe un angulo, calcula si es externo o interno
	y devuelve solo un angulo interno"""
	
	if angle > 180:
		return 360-angle

	else: return angle


def calculate_angle(
		az1:float, 
		az2:float
		)-> str:
	
	"""Recibe dos angulos azimutales que delimitan un punto 
	para encontrar el angulo interno de ese punto, lo retorna como string"""

	#Tiene en cuenta el orden en que se encuentran los púntos,
	#y retorna el valor y si es un error negativo o positivo
	if az1 > az2:
		angle = (az1 - az2)

		return f'+{definite_inter_angle(angle)}'
			
	elif az1 == az2:
		return 0
	else: 
		angle = (az2 - az1)
		return f"-{definite_inter_angle(angle)}"
	

def calculate_angular_error(
		**kargs
		)->float:
	"""Recibe 3 puntos de cierre el 1, el 4 y 1 prima, y retorna el error angular"""
	point1 = kargs.get('p1')
	point1_p = kargs.get('p1_prime')
	point4 = kargs.get('p4')

	#Calcula los azimuts del punto 4 con p1 y p1-prima, luego a traves de la funcion calculate_angle,
	# calcula el angulo interno formado por esos 3 puntos

	angle_error = calculate_angle(

				calculate_azimut([point4, point1]),
				calculate_azimut([point4, point1_p])
			)
	
	return angle_error

