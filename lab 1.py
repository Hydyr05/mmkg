def is_self_intersecting(polygon):
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        for j in range(i + 2, n):
            x3, y3 = polygon[j % n]
            x4, y4 = polygon[(j + 1) % n]
            if do_segments_intersect((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
                return True
    return False

def do_segments_intersect(p1, p2, p3, p4):
    def orientation(p1, p2, p3):
        return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])

    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)

    if (o1 > 0 and o2 < 0) or (o1 < 0 and o2 > 0) or (o3 > 0 and o4 < 0) or (o3 < 0 and o4 > 0):
        return True
    elif o1 == 0 and is_point_on_segment(p1, p2, p3):
        return True
    elif o2 == 0 and is_point_on_segment(p1, p2, p4):
        return True
    elif o3 == 0 and is_point_on_segment(p3, p4, p1):
        return True
    elif o4 == 0 and is_point_on_segment(p3, p4, p2):
        return True
    else:
        return False

def is_point_on_segment(p1, p2, p3):
    if min(p1[0], p2[0]) <= p3[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p3[1] <= max(p1[1], p2[1]):
        return True
    else:
        return False

polygon = [(2, 4), (-5, -4), (3, 1), (4, 0), (0, 4)]
if is_self_intersecting(polygon):
    print("Полигон является самопересекающимся.")
else:
    print("Полигон не является самопересекающимся.")
