# function to define if leap year
def leap_year(en_year: int) -> bool:
    """
    To return True if year is leap
    and False otherwise
    """
    if en_year % 4 == 0:
        if en_year % 400 == 0:
            return True
        elif en_year % 100 != 0:
            return True
    return False

# user input
if __name__ == "__main__":
    input_year = int(input("Please enter your year: "))
    if leap_year(input_year):
        print("This is leap year")
    else:
        print("This is not leap year")
