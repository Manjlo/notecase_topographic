from math import sqrt
from models_.main import Point, CoordinatesValues

def most_likely_value(
		points:list[Point]
		)->list[float]:

	"""Recibe una lista de puntos, retorna un lista con los
	valores mas probable de nortes y estes"""
	
	#Se inician las variables en 0
	[y_total_sum, x_total_sum] = [0, 0]

	#Se calcula la sumatoria y luego se retornan los valores dividios por el total de valores
	for point in points:
		y_total_sum += point.north
		x_total_sum += point.east

	return [x_total_sum/len(points), y_total_sum/len(points)]

def residual_list(
		points: list[Point], 
		likely_values: list[list[float]]

		)->list[list[float]]:

	"""Recibe una lista de puntos y una lista de valores probables,
	 retorna una lista de nortes y estes residuales"""

	north_residual_list = []
	east_residual_list = []

	for point in points:
		north_residual_list.append(point.north - likely_values[1])
		east_residual_list.append(point.east - likely_values[0])

	return [east_residual_list, north_residual_list]


def quadratic_middle_error(
		residual_list:list[list[float]], 
		)->float:

	"""Recibe una lista con 2 listas de errores en cada coordenada
	 y un lista de valores medianos de cada lista"""

	x_sumatory = 0
	y_sumatory = 0
	east_residual_list= residual_list[0]
	north_residual_list = residual_list[1]
	n = len(east_residual_list)
	for i in range(n):

		x_sumatory += east_residual_list[i]**2
		y_sumatory += north_residual_list[i]**2

	x_quadratic_error = sqrt(x_sumatory/n)
	y_quadratic_error = sqrt(y_sumatory/n)

	return [x_quadratic_error, y_quadratic_error]

def get_quadratic_middle_error(
		points: list[Point]
		)->float:

	"""Recibe una lista de puntos y 
	retorna el error medio cuadratico de las estes y de las nortes"""

	mp = most_likely_value(points)
	pi = residual_list(points, mp)
	[x_quadratic_error, y_quadratic_error] = quadratic_middle_error(pi)

	return CoordinatesValues(x=x_quadratic_error, y=y_quadratic_error)

def get_standard_desviation(
		points: list[Point]
		)->list[float]:
	
	"""Recibe una lista de puntos y retorna la desviacion
	estandard de las medidad nortes y estes"""

	#recibe los valores necesarios y inicia las sumatorias
	mp = most_likely_value(points)
	pi = residual_list(points, mp)
	x_sumatory = 0
	y_sumatory = 0

	#Suma cada valor de estes y nortes de la lista pi
	for i in range(len(pi[0])):
		x_sumatory += pi[0][i]**2
		y_sumatory += pi[1][i]**2
	
	x_standard_desviation = sqrt(x_sumatory/(len(pi)-1))
	y_standard_desviation = sqrt(y_sumatory/(len(pi)-1))

	return CoordinatesValues(x= x_standard_desviation, y= y_standard_desviation)

	











