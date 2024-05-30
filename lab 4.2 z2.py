import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Задаем точки
points = np.array([
    [-4, 1],
    [-2, 8],
    [-1, 7],
    [2, 0],
    [3, 3]
])

# Создаем триангуляцию Делоне
tri = Delaunay(points)

# Рисуем точки и триангуляцию
plt.figure()
plt.triplot(points[:,0], points[:,1], tri.simplices, color='red')
plt.plot(points[:,0], points[:,1], 'o')

# Аннотируем точки
for i, point in enumerate(points):
    plt.text(point[0], point[1], f'A{i+1}', fontsize=12, ha='right')

plt.gca().set_aspect('equal')
plt.show()
f