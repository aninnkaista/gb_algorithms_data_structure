def get_line_params(point_1: tuple, point_2: tuple):
    """
    Returns k and b to 2 decimal places for y = kx+b given coordinates of 2 points as tuples
    based on 2 equations
    y1 = k*x1 + b
    y2 = k*x2 + b
    k = (y1 - b)/x1
    y2 = (y1 - b)/x1 * x2 + b
    y2 = y1 / x1 * x2 - b*x2 / x1 + b
    y2 - y1/x1 * x2 = b(1 - x2/x1)"""
    x1, y1 = point_1
    x2, y2 = point_2
    b = (y2 - y1 / x1 * x2) / (1 - x2 / x1)
    k = (y1 - b) / x1
    return round(k, 2), round(b, 2)

if __name__ == '__main__':
    # to get input
    x1, y1 = map(float, input('Enter x1, y1 for the first point: ').strip().split())
    x2, y2 = map(float, input('Enter x2, y2 for the second point: ').strip().split())
    k, b = get_line_params((x1, y1), (x2, y2))
    if b > 0:
        print(f'Equation is y={k}x + {b}')
    else:
        print(f'Equation is y={k}x {b}')