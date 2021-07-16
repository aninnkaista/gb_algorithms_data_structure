# to import modules
import string

# function based on 2 letters
"""Finding the index of the letters in the alphabet
and the distance between them
input two letters, each one as a string
output index_1, index_2 and distance
"""
def get_letters(a: str, b: str):
    all_letters = string.ascii_lowercase
    # to get all letters to lowercase
    a = a.lower()
    b = b.lower()
    # index starts with 0
    index_1 = all_letters.index(a) + 1
    index_2 = all_letters.index(b) + 1
    dif_index = abs(index_2 - index_1)
    return index_1, index_2, dif_index

if __name__ == "__main__":
    a, b = input("Please enter two letters: ").strip().split()
    index_a, index_b, dif_index = get_letters(a, b)
    print(f"The index of the first letter is {index_a}",
          f"The index of the second letter is {index_b}",
          f"The distance between letters is {dif_index}",
          sep="\n")
