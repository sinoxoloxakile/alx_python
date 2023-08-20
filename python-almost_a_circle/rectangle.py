class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = integer_validator(width)
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = integer_validator(height)
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = integer_validator(x)
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = integer_validator(y)