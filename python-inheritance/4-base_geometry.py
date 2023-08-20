"""
    this is a semple class to represent a empty class
"""
class BaseGeometry:
    """
    this is a semple class to represent a empty class
    """
    pass
    def __dir__(cls):
        """
        this is a semple class to represent a empty class
        """
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != '__init_subclass__']
    def area(self):
        """
        this is a semple class to represent a empty class
        """
        raise Exception("area() is not implemented")