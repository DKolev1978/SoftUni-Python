def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    if not isinstance(length, int) and isinstance(width, int):
        return f"Enter valid values!"
    else:
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))
