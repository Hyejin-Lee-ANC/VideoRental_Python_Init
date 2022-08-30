class Movie(object):

    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, arg):
        self._price_code = arg

    def get_title(self):
        return self._title


