"""
You are given 4 points A, B, C and D in a 3-dimensional cartesian coordinate system.
you are required to find the angle between the planes made by the points A, B, C and B, C, D (use degrees not radian).
Let the angle be phi, then.

cos(phi) = (X.Y) / |X||Y| (. is the notation of dot product).
where X = (B - A)x(C - B) and Y = (C - B)x(D -C). (x is the notation of cross product).

Sample Input:
0 4 5
1 7 6
0 5 9
1 7 2

Sample Output:
8.19
"""
from __future__ import annotations

import math


class Points(object):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other: Points) -> Points:
        return Points(
            x=self.x - other.x,
            y=self.y - other.y,
            z=self.z - other.z
        )

    def dot(self, other: Points) -> int:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: Points) -> Points:
        return Points(
            x=self.y * other.z - self.z * other.y,
            y=self.z * other.x - self.x * other.z,
            z=self.x * other.y - self.y * other.x
        )

    def absolute(self) -> float:
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    X = (b - a).cross(c - b)
    Y = (c - b).cross(d - c)
    angle = math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))

    print("%.2f" % math.degrees(angle))
