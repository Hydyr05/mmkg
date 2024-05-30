import numpy as np
import matplotlib.pyplot as plt

# Задаем точки полигона
points = np.array([
    [0, 0],  # A1
    [2, 1],  # A2
    [1, 1],  # A3
    [-2, 2],  # A4
    [-1, 1],  # A5
    [-1, -1]  # A6
])

# Хорды для разбиения на выпуклые части
chords = [
    (0, 2),  # A1A3
    (2, 4)   # A3A5
]

# Рисуем полигон
plt.figure()
plt.plot(*zip(*(points.tolist() + [points[0].tolist()])), marker='o', color='black')

# Рисуем хорды
for chord in chords:
    p1, p2 = points[chord[0]], points[chord[1]]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'b-', lw=2)

# Аннотируем точки
for i, point in enumerate(points):
    plt.text(point[0], point[1], f'A{i+1}', fontsize=12, ha='right')

plt.gca().set_aspect('equal')
plt.show()
