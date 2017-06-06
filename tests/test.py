from catalog.apartment import Apartment


sites = ['test1', 'test2']

def data_for_all(example, st, file):
    '''
    add element to class
    :return:
    '''

    example.add(st, read_file(file))


def read_file(file_name):
    d = []
    with open(file_name, 'r', encoding='utf-8') as f:
        el = eval(f.readline())
        try:
            while el is not None:
                d.append(el)
                el = eval(f.readline())
        except:
            pass
    return d


h = Apartment()
#data_for_all(h, 'tester.txt')

with open('result213.txt', 'w') as t:
    for el in ['test1', 'test2']:
        t.write('************' + el + '************\n')
        #data_for_all(apartments1, ('DATA_by_price_asc_'+ el + '.txt'))
        #data_for_all(apartments1, ('DATA_by_price_desc_'+ el + '.txt'))
        data_for_all(h, el, ( el + '.txt' ))
        t.write('number = ' + str(h.number(el))+ '\n')
        print('number ')
        #print(apartments1.price_for_state('miami'))
        t.write('average price = ' + str(h.average_price(el))+ '\n')
        print('av')
        t.write('middle price = ' + str(h.middle_price(el)) + '\n\n')
        print('middle')
    t.write('number = ' + str(h.number('test1'))+ '\n')