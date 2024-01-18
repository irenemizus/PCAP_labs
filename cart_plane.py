import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vert_list = [vertice1, vertice2, vertice3]

    def perimeter(self):
        per = 0
        # for v in self.__vert_list:
        #     for v1 in self.__vert_list:
        #         per += math.hypot(v.getx() - v1.getx(), v.gety() - v1.gety())
        # return per / 2.0

        for i in range(len(self.__vert_list)):
            vi = self.__vert_list[i]
            vn = self.__vert_list[(i+1) % len(self.__vert_list)]
            per += math.hypot(vn.getx() - vi.getx(), vn.gety() - vi.gety())

        return per


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())



