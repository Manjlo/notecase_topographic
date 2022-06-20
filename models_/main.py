from pydantic import BaseModel, validator
from typing import Optional


""" Utilizo pydantic para crear modelos por que me permite manejar los errores de tipo que se puedan obtener, y 
ademas permite crear validaciones extra para los tipos de datos ingresados.
"""

class Point(BaseModel):
	name  : str 
	north : float
	east  : float

#se crea una validacion que busca que siempre el nombre ingresado sea mayuscula
	@validator('name')
	def name_must_be_upper(cls, v):
		upper_name = v.upper()
		return upper_name
	
class Side(BaseModel):
	name:Optional[str] = None
	distance:float
	azimut: float

class Close_error(BaseModel):
	points: list[Point]
	angle_error: str
	x_diference: float
	y_diference: float

class PolygonBase(BaseModel):
	points: list[Point]

	#validacion extra que permitira que siempre la lista de puntos ingresados sea igual a 5
	@validator('points')
	def points_must_be_greather_or_equal_than_4(cls, points):
		if len(points)!=5:
			raise ValueError('la cantidad de puntos ingresados no debe de ser mayor o menor a 5')
		return points

class PolygonCreate(PolygonBase):
	pass

class CoordinatesValues(BaseModel):
	y: float
	x:float

class Polygon(PolygonBase):
	area:float
	sides: list[Side]
	close_error: Close_error
	quadratic_middle_error: CoordinatesValues
	standard_deviation: CoordinatesValues
