# import random
# import string
#
# characters = string.ascii_uppercase + string.digits
#
# while True:
#     choice = input("Press Enter for a code (q to quit): ")
#
#     if choice.lower() == "q":
#         break
#
#     code = (
#         "".join(random.choices(characters, k=2)) + "-" +
#         "".join(random.choices(characters, k=2)) + "-" +
#         "".join(random.choices(characters, k=2)) + "-" +
#         "".join(random.choices(characters, k=4))
#     )
#
#     print(code)
#

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