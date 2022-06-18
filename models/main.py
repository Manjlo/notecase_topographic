from pydantic import BaseModel, validator
from typing import Optional

from work_logic.handle_points import calculate_azimut

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
	points: list[Point]
	name:Optional[str] = None
	distance:float
	azimut: float

#Esta "validacion" permitira crear un nombre ideal para cada lado del poligono
	@validator('name')
	def create_name(cls, v):
		return 'points[0]'+ "to" + 'points[1]'

class Close_error(BaseModel):
	points: list[Point]
	angle_error_value: float
	x_diference: float
	y_diference: float

class PolygonBase(BaseModel):
	points: list[Point]

	#validacion extra que permitira que siempre la lista de puntos ingresados sea igual a 5
	@validator('points')
	def points_must_be_greather_or_equal_than_4(cls, points):
		if len(points)!=5:
			raise ValueError('la cantidad de puntos ingresados no debe de ser mayor o menor a 5')

class PolygonCreate(PolygonBase):
	pass
	#esquema de ejemplo de como deben de ser pasados los puntos en el modelo PolygonCreate
	class Config:
		schemas_examples ={
			'points': 
				[
					{
						"name": "P1",
						"north": 1234567.1, 
						"east": 1234567.1, 
					},

					{
						"name": "P2",
						"north": 1234567.1, 
						"east": 1234567.1, 
		
					},

					{
						"name": "P3",
						"north": 1234567.1, 
						"east": 1234567.1, 
		
					},

					{
						"name": "P4",
						"north": 1234567.1, 
						"east": 1234567.1, 
		
					},
					{

						"name": "P1'",
						"north": 1234567.1, 
						"east": 1234567.1, 
		
					}

				]
		}

class Polygon(PolygonBase):
	area:float
	sides: list[Side]
	close_error: Close_error
	quadratic_middle_error: float
	standard_deviation: float









