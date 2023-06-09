# Password Generator Project
from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""


def generate_password():
    global password
    pass_list = []
    pass_letters = [choice(letters) for _ in range(randint(9, 10))]
    pass_nums = [choice(numbers) for _ in range(randint(2, 4))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_list = pass_symbols + pass_nums + pass_letters
    shuffle(pass_list)
    password = "".join(pass_list)
    return password



