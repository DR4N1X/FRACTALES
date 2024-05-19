from turtle import *

shape("turtle")
speed(0)

def tree(size, levels, angle):
	if levels == 0:
		color("green")
		dot(size)
		color("black")
		return

	forward(size)
	right(angle)

	tree(size * 0.8, levels - 1, angle)

	left(angle * 2)

	tree(size * 0.8, levels - 1, angle)

	right(angle)
	backward(size)


def snowflake_side(length, levels):
	if levels == 0:
		forward(length)
		return

	length /= 3.0
	snowflake_side(length, levels - 1)
	left(60)
	snowflake_side(length, levels - 1)
	right(120)
	snowflake_side(length, levels - 1)
	left(60)
	snowflake_side(length, levels - 1)


def create_snowflake(sides, length):
	colors = ["black", "black", "black", "black", "black"]
	for i in range(sides):
		color(colors[i])
		snowflake_side(length, sides)
		right(360 / sides)
	
''' 
	si aumentas n en create_snowflake(n, 200)
	el tamaño del arbol se aumenta como a su vez
	tiene que aumentar la cantidad de colores
	que se le pone en colors = [x]
'''

create_snowflake(5, 200)

mainloop()