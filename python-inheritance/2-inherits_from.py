"""
semple function has a method to check if object is an kind of a class
"""
def inherits_from(obj, a_class):
    """
    method to check if object is an instance of a class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class