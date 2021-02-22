def lon_to_m(degree):
    Point = [-122.9849,49.1293]
    return (degree-Point[0])/(1/85000)