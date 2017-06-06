
from catalog.arrays import DynamicArray
from catalog.platform_element import Platform_element
class Apartment_example():
    def __init__(self ):

        self.table = dict()
        self.prices = {}

    def add(self, state, adv):
        '''
        add state and their adv
        :param state: str
        :param adv: dynamicArray
        :return: None
        '''
        if state not in self.table:
            self.table[state] = DynamicArray()
        for el in adv:
            #print(el)
            #print(el, type(el))
            self.table[state].append(Platform_element(el['name'], state, el['url'], el['where'], el['price'],
                                                      el['geotag'], el['has_image'], el['has_map']))

    def mapped(self,state, percentage= False):
        if state in self.table:
            counter = 0
            for el in self.table[state]:
                if el.map():
                    counter += 1
            # print(counter)
            if not percentage:
                return counter
            else:
                return counter, round(counter*100/self.number(state),3)