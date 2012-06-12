class Tapas(object):
    def __init__(self, name):
        self.name = name

class Restaurant(object):
    def __init__(self, name, *menu):
        self.name = name
        self.menu = menu

class MontrealSiTdsMeeting(object):
    def __init__(self, date, restaurant):
        self.owners = ('Alan', 'Miquel')
        self.__gathering = date
        self.__restaurant = restaurant

    def gotTapas(self):
        goodItems = filter(lambda item: isinstance(item, Tapas), self.__restaurant.menu)
        if len(goodItems) > 0:
            return True
        return False

    def available(self, date=None):
        if date or self.__gathering:
            return True
        return False

    def ImIn(self):
        if self.available() and self.gotTapas():
            return True
        return False

def main():
    restaurant = Restaurant("Club Espagnol du Quebec", *[Tapas(t) for t in ['pulpo', 'tortilla de patatas', 'paella valenciana']])
    spanishLunch = MontrealSiTdsMeeting('06-14-12', restaurant)
    print spanishLunch.ImIn()

if __name__ == '__main__':
    main()