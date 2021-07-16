# import modules

# function to get number of letter in alphabet
import string


def get_letter_number(num: int) -> str:
    """
    To get letter in the alphabet from its number:
    input is a number
    output is correspoding letter
    """
    all_letters = string.ascii_lowercase
    # indexing start from 0
    let = all_letters[num - 1]
    return let

if __name__ == "__main__":
    num = int(input("Enter number of a letter: ").strip())
    let = get_letter_number(num)
    print(f"Letter is {let}")