def equilateral(sides):
    return triangle(sides) and sides[0] == sides[1] and sides[1] == sides[2]


def isosceles(sides):
    return triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])


def scalene(sides):
    return triangle(sides) and sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]


def triangle(sides):
    return sides[0]+sides[1] > sides[2] and sides[1]+sides[2] > sides[0] and sides[0]+sides[2] > sides[1]