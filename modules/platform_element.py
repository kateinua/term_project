class Platform_element:
    def __init__(self, name, state, url, where,  price=None, geotag=None, picture=False, map = False, free=False):
        self._name = name
        self._state = state
        self._url = url
        self._where = where
        if price != None:
            self._price = int(price[1:])
        else:
            self._price = price
        self._geotag = geotag
        self._picture = picture
        self._map = map
        self._free = free

    def name(self):
        return self._name
    def state(self):
        return self._state
    def url(self):
        return self._url
    def where(self):
        return self._where
    def price(self):
        return self._price
    def geotag(self):
        return self._geotag
    def picture(self):
        return self._picture
    def map(self):
        return self._map
    def free(self):
        return  self._free
