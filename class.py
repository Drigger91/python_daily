import math
class Point:
    def __init__(self, x, y) -> None:
        self.x = x;
        self.y = y;
    def print(self):
        print(f'x-cordinate {self.x}, y-cordinate {self.y}')
    def get_distance(self, a) -> float :
        if not isinstance(a, Point):
            raise TypeError("Not a valid point")
        dx = self.x - a.x;
        dy = self.y - a.y;
        return math.sqrt(dx ** 2 + dy ** 2);
        



p = Point(10, 20);
p.print();
x = p.get_distance(Point(10, 0));

print(x);

## Try-catch statements

try : 
    p.get_distance("");
except TypeError:
    print("Please pass a valid pointer")