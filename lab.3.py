import numpy as np

# Углы поворота вокруг осей Ox, Oy, Oz
alpha = -np.pi / 6
beta = np.pi / 4
gamma = 0

# Матрица поворота вокруг оси Ox
R_x = np.array([
    [1, 0, 0],
    [0, np.cos(alpha), -np.sin(alpha)],
    [0, np.sin(alpha), np.cos(alpha)]
])

# Матрица поворота вокруг оси Oy
R_y = np.array([
    [np.cos(beta), 0, np.sin(beta)],
    [0, 1, 0],
    [-np.sin(beta), 0, np.cos(beta)]
])

# Матрица поворота вокруг оси Oz
R_z = np.array([
    [np.cos(gamma), -np.sin(gamma), 0],
    [np.sin(gamma), np.cos(gamma), 0],
    [0, 0, 1]
])

# Комбинированная матрица поворота
R = np.dot(np.dot(R_x, R_y), R_z)

# Вывод матрицы
print("Матрица аксонометрического ортогонального проецирования:")
print(R)
