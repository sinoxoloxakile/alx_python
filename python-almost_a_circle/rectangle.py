"""
    This module to creates a smple class rectangle
"""
from models.base import Base

class Rectangle(Base):
    """
    class inherits frombase
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate values"""
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        super().__init__(id)


    @property
    def height(self):
        """
            mathed getter to get private width
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            mathed getter to get private width
        """
        self.toValidation('height', value)
        self.__height = value
    @property
    def width(self):
        """
            mathed getter to get private width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            mathed getter to get private width
        """
        self.toValidation('width', value)
        self.__width = value


    @property
    def y(self):
        """
            mathed getter to get private width
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            mathed getter to get private width
        """
        self.toValidation('y', value)
        self.__y = value
    
    @property
    def x(self):
        """
            mathed getter to get private width
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            mathed getter to get private width
        """
        self.toValidation('x', value)
        self.__x = value

    @staticmethod
    def toValidation(name, value):
        """
            to validation values of height and weight and x and y
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and (name == 'x' or name == 'y'):
            raise ValueError("{} must be >= 0".format(name))
        if value <= 0 and name != 'x' and name != 'y':
            raise ValueError("{} must be > 0".format(name))
        
    def area(self):
        """
            to get area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            Update the class Rectangle by adding the public method def 
            display(self): that prints in stdout the Rectangle instance with
            the character # - you don’t need to handle x and y here.
        """
        for x in range(self.__y):
            print("")
        for z in range(self.__height):
            print(" "*self.__x + "#"*self.__width)


    def __str__(self):
        """
            Update the class Rectangle by overriding the __str__ method so that it
            returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))
    
    def update(self, *args, **kwargs):
        """
        updates the values using args and kwargs
        """
        attrbut = [ "id","width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attrbut[i], arg)

        for key, value in kwargs.items():
            if key in attrbut:
                setattr(self, key, value)