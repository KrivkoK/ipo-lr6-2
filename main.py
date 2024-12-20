import random

# Задаем размеры матрицы
height = random.randint(4, 8)
width = random.randint(4, 8)

# Исходный список значений
values = [-15, -4, -2, -7, 0, 3, 5, 12, 7]

# Создаем двумерную матрицу и заполняем ее значениями из списка
matrix = [[random.choice(values) for _ in range(width)] for _ in range(height)]

# Выводим матрицу в форматированном виде
print("Сгенерированная матрица:")
for row in matrix:
    print(" | ".join(f"{str(elem):>4}" for elem in row))

# Считаем сумму всех нечетных элементов
odd_sum = sum(elem for row in matrix for elem in row if elem % 2 != 0)

# Выводим сумму нечетных элементов
print(f"\nСумма всех нечетных элементов: {odd_sum}")
