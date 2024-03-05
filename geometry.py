# This is a module that can calculate the area of a circle and return the hypotenuse of a right triangle
def circle_area(radius):
    """
    Will return the approximate area of a circle with the given radius
    Did not use math.pi as it doesn't make a difference
    """
    return 3.14159265358979323846264338 * radius**2

def get_hypotenuse(leg1, leg2):
    """
    Will return the length of the hypotenuse of a right triangle
    with the given leg lengths.
    Did not use math.sqrt as it doesn't make a difference
    """
    return (leg1**2 + leg2**2)**0.5