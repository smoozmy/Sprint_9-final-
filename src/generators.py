import random
import string

from src.data import Data


class Generators:

    @staticmethod
    def generate_email():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        return f"test-{random_string}@email.ru"

    @staticmethod
    def generate_text(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_user():
        return {
            "email": Generators.generate_email(),
            "password": Data.PASSWORD,
        }

