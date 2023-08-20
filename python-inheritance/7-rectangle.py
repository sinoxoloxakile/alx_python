class BaseGeometry:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError
    def perimeter(self):
        raise NotImplementedError
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a new rectangle.
        Args:
            width: The width of the rectangle in pixels.
            height: The height of the rectangle in pixels.
        """
        self._width = integer_validator(width)
        self._height = integer_validator(height)
    def area(self):
        """
        Returns the area of the rectangle in pixels.
        Returns:
            The area of the rectangle in pixels.
        """
        return self._width * self._height
    def __repr__(self):
        return "[Rectangle] {}/{}".format(self._width, self._height)
    def __str__(self):
        return self.__repr__()