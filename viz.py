# Импортируем библиотеку для построения графиков
import matplotlib.pyplot as plt

# === Функция для чтения данных из файла ===
def read_output_file(filename):
    # Открываем файл и читаем все непустые строки
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]  # Убираем пробелы и пустые строки

    # Первая строка — количество кластеров (k)
    k = int(lines[0])

    # Список для хранения координат центров кластеров
    centers = []

    # Начинаем читать с первой строки после количества кластеров
    i = 1

    # Читаем k строк с координатами центров
    for _ in range(k):
        x, y = map(float, lines[i].split())  # Преобразуем строки в числа
        centers.append((x, y))  # Добавляем центр кластера в список
        i += 1

    # Следующая строка — количество точек (n)
    n = int(lines[i])
    i += 1

    # Читаем n строк с точками и информацией о кластере
    points = []
    for _ in range(n):
        x, y, v = lines[i].split()  # x и y — координаты, v — номер кластера
        points.append((float(x), float(y), int(v)))  # Добавляем как кортеж
        i += 1

    # Возвращаем список центров и список точек
    return centers, points

# === Функция для построения графика ===
def plot_clusters(centers, points):
    # Находим максимальный номер кластера, чтобы выбрать достаточно цветов
    max_cluster = max(v for _, _, v in points)

    # Получаем палитру цветов, с нужным числом кластеров
    # 'tab10' — стандартная палитра с 10 цветами
    colors = plt.colormaps['tab10'].resampled(max_cluster + 1)

    # Рисуем все точки по одному
    for x, y, v in points:
        plt.scatter(x, y, color=colors(v), s=20)  # s — размер точки

    # Разделяем координаты центров по осям X и Y
    cx, cy = zip(*centers)

    # Рисуем центры кластеров — большие чёрные крестики
    plt.scatter(cx, cy, color='black', marker='X', s=100, label='Центры')

    # Добавляем подписи и сетку
    plt.title("K-Means++ Clustering")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()  # Показываем легенду (обозначение центров)

    # Показываем график
    plt.show()

# === Точка входа ===
# Сначала читаем данные из output.txt
centers, points = read_output_file("output.txt")

# Затем строим визуализацию
plot_clusters(centers, points)
