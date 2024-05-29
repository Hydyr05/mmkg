def is_point_inside_polygon(point, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n+1):
        p2x, p2y = polygon[i % n]
        if point[1] > min(p1y, p2y):
            if point[1] <= max(p1y, p2y):
                if point[0] <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (point[1]-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or point[0] <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

polygon = [(2, 4), (-5, -4), (3, 1), (4, 0), (0, 4)]
points = [(2, 2), (3, -1), (1, 0), (-2, -3), (-3, 1), (0, 0)]

for point in points:
    if is_point_inside_polygon(point, polygon):
        print(f"Точка {point} лежит внутри полигона.")
    else:
        print(f"Точка {point} лежит снаружи полигона.")
