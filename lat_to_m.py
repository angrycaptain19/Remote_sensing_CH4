def lat_to_m(degree):
    Point = [-122.9849,49.1293]
    return (degree-Point[1])/(1/111000)