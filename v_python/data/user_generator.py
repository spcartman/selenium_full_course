from random import choice, randrange
import string
from model.user import User


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits
    return prefix + "".join([choice(chars) for i in range(randrange(1, maxlen))])


def generate_user():
    return User(f_name=rand_string('first_', 30), l_name=rand_string('last_', 30), address=rand_string('address_', 50),
                postcode=randrange(10000, 100000), city=rand_string('city_', 20), country='US',
                email=(rand_string('email_', 20) + '@mejl.kom').replace(' ', ''),
                phone='+' + str(randrange(10000000, 20000000)), password=rand_string('pwd', 50))
