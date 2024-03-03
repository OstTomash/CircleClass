class Circle:
    """A simple class representing a circle.

    This class allow users to create instance of class Circle and get area.

    Attributes:
        - radius (int): radius of the circle

    Class variable:
        - PI (float): constant with value 3.14

    Methods:
        - __init__(radius): Initializes the circle with the given radius
        - get_area(): Returns the area of circle
        - __str__(): Returns the string representation of instance

    Example usage:
    >>> example_circle = Circle(10)
    >>> example_area = example_circle.get_area()
    >>> print(example_area)
    314.0
    """
    PI = 3.14

    def __init__(self, radius):
        """Initializes the circle with the given radius"""
        self.radius = radius

    def get_area(self):
        """Returns the area of circle"""
        return self.PI * (self.radius ** 2)

    def __str__(self):
        """Returns a string representation of instance"""
        return f"Circle with radius {self}"


circle = Circle(10)
area = circle.get_area()

print(area)
