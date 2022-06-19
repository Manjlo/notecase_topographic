from models_.main import Point, PolygonBase, PolygonCreate
from work_logic.handle_polygon import create_new_polygon


p1 = Point(name = 'p1',north= 1000,east=500)
p2 = 	Point(name = 'p2',north= 1167.723,east=370.508)
p3 = 	Point(name = 'p3',north= 1091.696,east=277.727)
p4 = 	Point(name = 'p4', north= 952.810, east=316.221)
p1_p =	Point(name = 'p1_p',north= 1000.56,east=499.983)

fake_data = [p1, p2, p3, p4, p1_p]

def create_polygon(points:list[Point]):
	polygon = create_new_polygon(points=points)
	return polygon



create_new_polygon(fake_data)

#print(fake_data)