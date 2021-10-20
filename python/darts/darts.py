def score(x, y):
    total = 10
    inner = 1
    middle = 5

    points = 0
    radius = get_radius(x, y)
    if radius > 10:
        return points
    elif 5 < radius <= 10:
        points = 1
    elif 1 < radius <= 5:
        points = 5
    else:
        points = 10
    return points


def get_radius(x, y):
    return (x ** 2 + y ** 2) ** 0.5
