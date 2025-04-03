class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        return 0

    def info(self):
        print("Figure info not available")

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def info(self):
        print(f'Square side length: {self.side_length}{self.unit}, area: {self.calculate_area()}{self.unit}².')

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def info(self):
        print(f'Rectangle length: {self.length}{self.unit}, width: {self.width}{self.unit}, area: {self.calculate_area()}{self.unit}².')

if __name__ == "__main__":
    figures = [
        Square(8),
        Square(3),
        Rectangle(9, 7),
        Rectangle(6, 10),
        Rectangle(5, 2)
    ]
    for figure in figures:
        figure.info()

