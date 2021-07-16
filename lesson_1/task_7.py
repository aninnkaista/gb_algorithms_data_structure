# function difining triangle type and its possibility

def get_triangle_type(a: float, b: float, c: float) -> str:
    """
    Based on the sides of the triangle (a, b, c) to define its type;
    if it is not possible to built triangle then return None
    """
    # to check if triangle exists, the sum of any 2 sides is bigger than the third side
    if a + b > c and a + c > b and c + b > a:
        # if yes then check triangle type
        if a == b == c:
            triangle_type = "equilateral"
        elif a == b or b == c or c == a:
            triangle_type = "isosceles"
        else:
            triangle_type = "scalene"
    else:
        triangle_type = None
    return triangle_type

# to get input from the user and print output
if __name__ == "__main__":
    a, b, c = map(float, input("Enter three measurements to check: ").strip().split())
    triangle_type = get_triangle_type(a, b, c)
    if triangle_type:
        print(f"Triangle of those measurements exists and it is {triangle_type}")
    else:
        print("Triangle of those measurements does not exist")