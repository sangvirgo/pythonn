from abc import ABC, abstractmethod

class Shape:
    def __init__(self, color='red', filled=True):
        self._color=color
        self._filled=filled
    def getColor(self):
        return self._color
    def setColor(self, color):
        self._color=color
    def isFilled(self):
        return self._filled
    def setFilled(self, filled):
        self._filled = filled

    def getArea(self):
        pass
    def getPerimeter(self):
        pass
    def to_String(self):
        return f"Shape[color={self._color}, filled={self._filled}]"

class Circle(Shape):
    def __init__(self,radius=1.0, color='red',  filled=True):
        super().__init__(color, filled)
        self._radius=radius
    def getRadius(self):
        return self._radius
    def setRadius(self, radius):
        self._radius = radius
    def getArea(self):
        return 3.14159 * (self._radius ** 2)
    def getPerimeter(self):
        return 2 * 3.14159 * self._radius
    def to_String(self):
        return f"Circle[{super().to_String()}, radius={self._radius}]"

class Rectangle(Shape):
    def __init__(self, color='red', filled=True, width=1.0, length=1.0):
        super().__init__(color, filled)
        self._width=width
        self._length=length
    def getWidth(self):
        return self._width
    def setWidth(self, width):
        self._width = width
    def getLength(self):
        return self._length
    def setLength(self, length):
        self._length = length
    def getArea(self):
        return self._width * self._length
    def getPerimeter(self):
        return 2 * (self._width + self._length)
    def to_String(self):
        return f"Rectangle[{super().to_String()}, width={self._width}, length={self._length}]"

if __name__=="__main__":
    circle = Circle(2.5, "blue", False)
    rectangle = Rectangle("green", True, 2.0, 3.0)
    print(circle.to_String())
    print(rectangle.to_String())