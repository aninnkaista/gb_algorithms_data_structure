# function of finding middle number among three
def find_middle_number(a: float, b: float, c:float) -> float:
    """Out of 3 entered different numbers it finds the middle one and return its value"""
    if a > b > c or c > b > a:
        return b
    elif a > c > b or b > c > a:
        return c
    else:
        return a

# user input
if __name__ == "__main__":
    a, b, c = map(float, input("Please enter three different numbers: ").split())
    print(f"The middle number is {find_middle_number(a, b, c)}")