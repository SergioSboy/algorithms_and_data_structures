class OrangeGarden:
    def __init__(self, width, height, plants):
        self.width = width
        self.height = height
        self.plants = plants

    def calculate_square_sizes(self):
        square_sizes = []
        for x, y in self.plants:
            left_distance = x
            right_distance = self.width - x
            top_distance = y
            bottom_distance = self.height - y
            size = min(left_distance, right_distance, top_distance, bottom_distance)
            square_sizes.append(size)
        return square_sizes


def main():
    # Считываем размеры оранжереи и количество растений
    W, H, N = map(int, input().split())

    # Считываем координаты растений
    plants = [tuple(map(int, input().split())) for _ in range(N)]

    # Создаем объект оранжереи
    orange_garden = OrangeGarden(W, H, plants)

    # Вычисляем размеры соответствующих квадратов
    square_sizes = orange_garden.calculate_square_sizes()

    # Выводим размеры квадратов в правильном порядке
    for size in square_sizes:
        print(size)


if __name__ == "__main__":
    main()