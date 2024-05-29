import numpy as np

# Нормальный вектор плоскости
normal_vector = np.array([1, -2, 1])

# Матрица оператора f
matrix = np.identity(3)  # Создаем единичную матрицу 3x3
matrix[:, 2] = 2 * normal_vector  # Умножаем третий столбец на 2

print("Матрица оператора f:")
print(matrix)
