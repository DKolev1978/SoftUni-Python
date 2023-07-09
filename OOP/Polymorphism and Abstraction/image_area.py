class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


a1 = ImageArea(7, 10)
print(a1.get_area())
a2 = ImageArea(35, 2)
print(a2.get_area())
a3 = ImageArea(8, 9)
print(a3.get_area())
print(a1 == a2)
print(a1 != a3)