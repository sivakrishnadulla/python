class Polygon:
    width = 0
    height = 0

    def set_values(self,width,height):
       Polygon.width = width
       Polygon.height = height

class Rectangle(Polygon):

    def Area(self):
        return self.width*self.height

class Triangle(Polygon):

    def Area(self):
        return (self.width*self.height)/2

rect = Rectangle()
tri = Triangle()

rect.set_values(13,15)
tri.set_values(12,15)

print("Area of Rectangle is ",rect.Area())
print("Area of Triangle is ",tri.Area())
