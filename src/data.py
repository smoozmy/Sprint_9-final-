import os


class Data:
    BASE_URL = os.getenv('BASE_URL', "https://foodgram-frontend-1.prakticum-team.ru/")
    PASSWORD = "parol123"
    EAT_TAGS = ["breakfast", "lunch", "dinner"]

    RECIPE = {
        "name": "Хот-Дог",
        "tags": ["breakfast", "lunch", "dinner"],
        "ingredients": {"булочки с кунжутом": 3},
        "cook_time": 5,
        "description": "Каждый дог немного хот",
        "photo": "hot_dog.jpeg"
    }