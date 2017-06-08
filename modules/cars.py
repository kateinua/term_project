
from arrays import DynamicArray
from platform_element import Platform_element
class Car():
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





    def refresh_price(self, other_state, other_adv = None):
        '''
        add prices from other_adv to price[other_state]
        if other_state is add to examle of class then other_adv None
        :param other_state: str
        :param other_adv: dynamicArray
        :return:
        '''
        if other_state not in self.table :
            kv = round(len(other_adv)/10)
            self.table[other_state] = DynamicArray()
            # multiply 1.5 for skipping more advertisments with None value
            self.table[other_state].append(other_adv[round(kv*1):-kv])
            self.prices[other_state] = []
            i = 0
            while i < len(self.table[other_state]):
                if self.table[other_state][i].price() == None:
                    self.table[other_state].remove_ind(i)

                else:
                    #print('gggggg'+str(int(self.table[other_state][i].price())))
                    self.prices[other_state].append(int(self.table[other_state][i].price()))
                    i += 1
        elif other_adv is None:
            #kv = round(len(other_adv)/10)
            i = 0
            if other_state not in self.prices:
                self.prices[other_state] = []
            if other_adv is None:
                other_adv = self.table[other_state]
                while i < len(other_adv):
                    #print(other_adv[i][0])
                    if other_adv[i].price() == None:
                        other_adv.remove_ind(i)
                    else:
                        # self.table[other_state].append(other_adv[i])
                        #print(other_adv[i], type(other_adv[i]))
                        self.prices[other_state].append((other_adv[i].price()))
                        i += 1
        else:
            kv = round(len(other_adv) / 10)
            i = kv
            if other_state not in self.prices:
                self.prices[other_state] = []
            if other_adv is None:
                other_adv = self.table[other_state]
                while i < len(other_adv) - kv:
                    # print(other_adv[i][0])
                    if other_adv[i].price() == None:
                        other_adv.remove_ind(i)
                    else:
                        # self.table[other_state].append(other_adv[i])
                        # print(other_adv[i], type(other_adv[i]))
                        self.prices[other_state].append((other_adv[i].price()))
                        i += 1



    def check_is_near_the_same(self, state, advert):
        i = 0
        count = 0
        procent = 0
        #print('fffffffff4')
        while i < (len(advert)/1.5) and procent < 45:
            #print(procent)
            if advert[i].price() == None:
                advert.remove_ind(i)
                continue
            elif advert[i].price() in self.prices[state]:
                count += 1
                procent = 100 * count/len(advert)

            i += 1
        if procent < 30:
            return False
        else:
            return True

    def average_price(self, state):
        if state in self.table:
            self.refresh_price(state)
            #print('refreshed')
            #kv = round(len(self.prices[state]) / 10)
            return round(sum(self.prices[state])/(len(self.prices[state])), 3)
        else:
            raise TypeError("Wrong state.")

    def middle_price(self, state):
        if state in self.table:
            self.prices[state].sort()
            #print(len(self.prices[state]), round(self.number(state)/2))
            return (self.prices[state][round(len(self.prices[state])/2)])
        else:
            raise TypeError("Wrong state.")

    def number(self, state):
        if state in self.table:

            #print(len(self.table[state]))
            return len(self.table[state])
        else:
            raise TypeError("Wrong state.")

    def price_for_state(self, state):
        if state in self.prices:
            #print('2\n')
            return self.prices[state]
        elif state in self.table:
            #print('1\n')
            self.refresh_price(state)
            return self.prices[state]
        else:
            raise KeyError

    def average_len_advert(self, state):
        if state in self.table:
            together = 0
            for el in self.table[state]:
                together += len(el.name())
            return round(together/(self.number(state)), 3)

    def most_popular_place(self,state,percentage=False):
        if state in self.table:
            d = {}
            for el in self.table[state]:
                if el.where() in d:
                    d[el.where()] += 1
                elif el.where() is not None:
                    d[el.where()] = 1
            if not percentage:
                return max(d)
            else:
                return max(d), round(d[max(d)]*100/self.number(state), 3)

    def geotaged(self, state, percentage = False):
        if state in self.table:
            counter = 0
            for el in self.table[state]:
                if el.geotag():
                    counter += 1
            if not percentage:
                return counter
            else:
                return counter, round(counter*100/self.number(state),3)

    def pictured(self, state, percentage=False):
        if state in self.table:
            #print('pictured',state)
            counter = 0
            for el in self.table[state]:
                if el.picture():
                    counter += 1
            #print(counter)
            if not percentage:
                return counter
            else:
                return counter, round(counter*100/self.number(state),3)

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


            #store = Apartment()