import string
import random


def gen_password():
    up = list(string.ascii_uppercase)
    down = list(string.ascii_lowercase)
    digits_ = list(string.digits+"_")
    up2 = random.sample(up, 2)
    down3 = random.sample(down, 3)
    digits_3 = random.sample(digits_, 3)
    values_for_code = digits_3 + down3 + up2
    random.shuffle(values_for_code)
    our_code = "".join(values_for_code)
    return our_code


print(gen_password())


