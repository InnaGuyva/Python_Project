from Rectangel import Rectangle, Square, Circle

rect_1 = Rectangle(15,7)
rect_2 = Rectangle(3,5)

print(rect_1.getArea())
print(rect_2.getArea())

sq_1 = Square(13)
sq_2 = Square(6)

print(sq_1.getAreaSq())
print(sq_2.getAreaSq())

cir_1 = Circle(2)
cir_2 = Circle(4)

print(cir_1.getAreaCir())
print(cir_2.getAreaCir())

figures = [rect_1, rect_2, sq_1, sq_2, cir_1, cir_2]
for figure in figures:
          print(figure.getAreaCir())
          print(figure.getAreaSq())
          print(figure.getArea())

