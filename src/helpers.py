class Helpers:

    @staticmethod
    def is_substr_in_list(substr: str, lst: list):
        for item in lst:
            if substr in item:
                return True
