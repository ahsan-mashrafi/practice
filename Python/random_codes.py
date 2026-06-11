import random
import string

letters = string.ascii_uppercase
numbers = string.digits
greek = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"

all_letters = letters + greek

while True:
    input("Press Enter to generate a code... ")

    code = (
        random.choice(all_letters) +
        random.choice(numbers) +
        "-" +
        random.choice(all_letters) +
        random.choice(numbers) +
        "-" +
        random.choice(all_letters) +
        random.choice(all_letters) +
        random.choice(numbers) +
        random.choice(numbers)
    )

    print(code)
