import random
import numpy as np
from PIL import Image


def generate_binary_matrix(rows, cols):
    matrix = np.random.randint(2, size=(rows, cols))  # Генерация матрицы из случайных 1 и 0
    return matrix


def save_matrix_as_bmp(matrix, filename):
    image_data = np.uint8(matrix) * 255  # Преобразование 1 и 0 в значения яркости (0 и 255)
    image = Image.fromarray(image_data, mode='L')  # Создание изображения из матрицы
    image.save(filename)  # Сохранение изображения в формате BMP


def save_matrix_as_txt(matrix, filename):
    np.savetxt(filename, matrix, fmt='%d')


if __name__ == '__main__':
    rows = 10
    cols = 10

    seed = 0
    random.seed(seed)
    np.random.seed(seed)

    filename = f'matrix_{rows}_{cols}_{seed}'

    matrix = generate_binary_matrix(rows, cols)
    matrix[0][0] = 1

    save_matrix_as_txt(matrix, filename + '.txt')

    inverted_matrix = np.logical_not(matrix).astype(int)
    save_matrix_as_bmp(inverted_matrix, filename + '.bmp')


#%%
