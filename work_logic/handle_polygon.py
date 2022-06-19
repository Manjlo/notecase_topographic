from models_.main import Point, Polygon, PolygonBase, PolygonCreate, Close_error, Side
from work_logic.close_error.angular_error import calculate_angular_error
from work_logic.handle_points import calculate_diferences, handle_side
from work_logic.close_error.statiscal_error import get_quadratic_middle_error, get_standard_desviation
from work_logic.polygon_props import calculate_area


def create_new_close_error(
			P1:Point, 
			P4:Point, 
			P1_p:Point
			)->Close_error:

	"""recibe 3 puntos, P1, P4, P1_prima. Retorna el error de cierre"""

	[y_diference, x_diference] = calculate_diferences(P1, P1_p)

	close_error = Close_error(
		points=[P1, P1_p, P4],
		angle_error= calculate_angular_error(p4=P4, p1=P1, p1_prime=P1_p),
		x_diference = x_diference,
		y_diference = y_diference
	)
	return close_error

def get_sides(
		points:list[Point]
		)->list[Side]:

	"""Recibe un lista de puntos y calcula el azimut y su distancia de cada combinacion de puntos"""
	sides = []
	for i in range(len(points)-1):
		sides.append(handle_side([points[i], points[i+1]]))
	return sides

def create_new_polygon(points:list[Point])->Polygon:
	"""Recibe una lista de puntos y retorna un diccionario de la clase Poligono"""
	P1 = points[0]
	P4 = points[3]
	P1_p = points[4]

	polygon = Polygon(
		points=points,
		area = calculate_area(points),
		sides=get_sides(points),
		close_error = create_new_close_error(
					P1=P1, 
					P4=P4, 
					P1_p= P1_p
					),
		quadratic_middle_error = get_quadratic_middle_error([P1, P1_p]),
		standard_deviation= get_standard_desviation([P1, P1_p])

	)
	print(polygon.dict())



