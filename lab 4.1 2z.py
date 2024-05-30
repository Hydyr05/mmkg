import matplotlib.pyplot as plt
import numpy as np

# Заданные координаты вершин многоугольника
vertices = np.array([
    [0, 0],  # A1
    [0, 3],  # A2
    [-3, 5], # A3
    [-5, 4], # A4
    [-2, 2], # A5
    [-3, 4]  # A6
])

# Дополнительная точка A3^1
extra_point = np.array([[-17/5, 24/5]])

# Определение хорд
# Хорды делят многоугольник на выпуклые части
chords = [
    (2, 3),  # A3A4
    (1, 4),  # A2A5
    (3, 5)   # A4A6
]

# Визуализация многоугольника и хорд
fig, ax = plt.subplots()

# Исходный многоугольник
polygon = plt.Polygon(vertices, closed=True, fill=None, edgecolor='black')
ax.add_patch(polygon)

# Хорды
for start, end in chords:
    line = plt.Line2D([vertices[start][0], vertices[end][0]], 
                      [vertices[start][1], vertices[end][1]], 
                      color='blue')
    ax.add_line(line)

# Дополнительная точка и связанные с ней хорды
extra_lines = [
    (2, 0),  # A3^1A1
    (2, 4),  # A3^1A5
    (2, 5)   # A3^1A6
]

for start, end in extra_lines:
    line = plt.Line2D([extra_point[0][0], vertices[end][0]], 
                      [extra_point[0][1], vertices[end][1]], 
                      color='blue')
    ax.add_line(line)

# Отображение точек
ax.plot(vertices[:, 0], vertices[:, 1], 'ko')  # Вершины многоугольника
ax.plot(extra_point[:, 0], extra_point[:, 1], 'ro')  # Дополнительная точка

# Настройки графика
ax.set_xlim(-6, 2)
ax.set_ylim(-1, 6)
ax.set_aspect('equal')
ax.grid(True)
plt.show()
