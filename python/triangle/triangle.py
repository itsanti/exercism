def equilateral(sides):
    return all([sides[0] == el and el != 0 for el in sides])


def isosceles(sides):
    if any([sides[0] == sides[1], sides[0] == sides[2], sides[1] == sides[2]]):
        if not any([el for el in sides if el == 1]):
            return True
    return False


def scalene(sides):
    return (not (equilateral(sides) or isosceles(sides)) and
            all([sides[0] + sides[1] > sides[2], sides[0] + sides[2] > sides[1], sides[1] + sides[2] > sides[0]]))
