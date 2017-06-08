#from catalog.arrays import DynamicArray
from apartment import Apartment
from jobs import Job
from cars import Car

sites_taken = {'delaware': ['delaware'],'maine':['maine'],'montana':['montana'],'newyork':['newyork'], 'vermont':['vermont'],
         'wyoming':['wyoming'], 'california': ['losangeles', 'sandiego'], 'illinois':['chicago'], 'texas': ['houston',
                                                                                                            'sanantonio',
                                                                                                            'dallas',
                                                                                                            'austin',
                                                                                                            'elpaso'],
         'pennsylvania':['philadelphia'], 'arizona':['phoenix'], 'florida' : ['jacksonville'], 'indiana' :
             ['indianapolis'], 'ohio' : ['columbus'], 'northcarolina': ['charlotte'], 'michigan':['detroit'],
         'tennessee': ['memphis'], 'massachusetts':['boston'], 'washington':['seattle'], 'colorado': ['denver']}
'''
sites = {'washington': ['seattle'], 'louisiana': ['neworleans', 'batonrouge'], 'california': ['losangeles',
                                                                                                  'sandiego', 'fresno',
                                                                                                  'sacramento',
                                                                                                  'bakersfield',
                                                                                                  'anaheim', 'santaana',
                                                                                                  'riverside',
                                                                                                  'stockton',
                                                                                                  'chulavista',
                                                                                                  'irvine', 'fremont',
                                                                                                  'sanbernardino'],
             'nebraska': ['omaha', 'lincoln'], 'newyork': ['newyork', 'buffalo'], 'idaho': ['boise'], 'pennsylvania':
                 ['philadelphia', 'pittsburgh'], 'indiana': ['indianapolis', 'fortwayne'], 'florida': ['jacksonville',
                                                                                                       'miami', 'tampa',
                                                                                                       'orlando',
                                                                                                       'st.petersburg',
                                                                                                       'hialeah'],
             'texas': ['houston', 'sanantonio', 'dallas', 'austin', 'elpaso',  'corpuschristi', 'plano',
                       'laredo', 'lubbock', 'garland', 'irving'], 'maryland': ['baltimore'], 'newjersey': ['newark',
                                                                                                           'jersey'],
             'hawaii': ['honolulu'], 'northcarolina': ['charlotte', 'raleigh', 'greensboro', 'durham', 'winston-salem'],
             'kansas': ['wichita'], 'illinois': ['chicago'], 'tennessee': ['memphis'], 'massachusetts': ['boston'],
             'ohio': ['columbus', 'cleveland', 'cincinnati', 'toledo'], 'oklahoma': ['tulsa'], 'virginia':
                 ['norfolk', 'chesapeake'], 'newmexico': ['albuquerque'], 'arizona': ['phoenix',
                                                                                                       'tucson',
                                                                                                       'chandler',
                                                                                                       'glendale',
                                                                                                       'scottsdale',
                                                                                                       'gilberttown'],
             'michigan': ['detroit'], 'oregon': ['portland'], 'wisconsin': ['milwaukee', 'madison'], 'alabama':
                 ['birmingham'], 'alaska': ['anchoragemunicipality'], 'colorado': ['denver', 'aurora'], 'kentucky':
                 ['louisville', 'lexington-fayette'], 'missouri': ['st.louis'], 'georgia': ['atlanta'],
             'nevada': ['lasvegas', 'henderson', 'reno', 'northlasvegas'], 'minnesota': ['minneapolis', 'st.paul']}
'''
sites = {'massachusetts': ['boston'], 'louisiana': ['neworleans'], 'washington': ['seattle'], 'nebraska': ['omaha'],
         'minnesota': ['minneapolis'], 'maryland': ['baltimore'], 'tennessee': ['memphis'], 'newmexico':
             ['albuquerque'], 'arizona': ['phoenix', 'tucson'], 'florida': ['jacksonville', 'miami'],
         'kansas': ['wichita'], 'texas': ['houston', 'sanantonio', 'dallas', 'austin', 'elpaso'],
         'oklahoma': ['tulsa'], 'michigan': ['detroit'], 'ohio': ['columbus', 'cleveland'], 'georgia': ['atlanta'],
         'pennsylvania': ['philadelphia'], 'illinois': ['chicago'], 'wisconsin': ['milwaukee'], 'colorado': ['denver'],  'nevada':
             ['lasvegas'], 'oregon': ['portland'], 'california': ['losangeles', 'sandiego',  'fresno',
                                                                  'sacramento',  'bakersfield'],
         'indiana': ['indianapolis'], 'kentucky': ['louisville'], 'northcarolina': ['charlotte', 'raleigh']}
def data_for_one(example, state,  file):
    '''
    add element to class
    :return:
    '''
    example.add(state, read_file(file))


def read_file(file_name):
    d = []
    with open(file_name, 'r', encoding='utf-8') as f:
        el1 = eval(f.readline())
        try:
            while el1 is not None:
                d.append(el1)
                el1 = eval(f.readline())
        except:
            return d
    return d
'''
add
number
average_price
'''
apartments1 = Apartment()
job1 = Job()
car1 = Car()
with open('result.txt', 'w') as t:
    for state in sites:
        t.write('************' + state + '************\n')
        #data_for_all(apartments1, ('DATA_by_price_asc_'+ el + '.txt'))
        #data_for_all(apartments1, ('DATA_by_price_desc_'+ el + '.txt'))
        for el in sites[state]:
            print(el)
            data_for_one(apartments1, state, ('data/DATA_by_date_'+ el + '.txt'))
            data_for_one(job1, state, 'data/DATA_by_jobs_' + el +'.txt')
            data_for_one(car1, state, 'data/DATA_by_cars_' + el +'.txt')
        t.write('number of apartment advertisments = ' + str(apartments1.number(state))+ '\n')
        #print('number ')
        #print(apartments1.price_for_state('miami'))
        t.write('average price = ' + str(apartments1.average_price(state))+ '\n')
        #print('av')
        t.write('middle price = ' + str(apartments1.middle_price(state)) + '\n')
        t.write('average length of advertisment = ' + str(apartments1.average_len_advert(state)) + '\n')
        try:
            k = apartments1.most_popular_place(state, True)
            t.write('the most popular place = ' + str(k[0])+' ' +str(k[1])+ '%\n')
        except UnicodeEncodeError:
            t.write("the most popular place is secret, "+ str(k[1]) + '%\n')
        k = apartments1.geotaged(state, True)
        t.write('number geotagged = ' + str(k[0])+' ' +str(k[1])+ '%\n')
        k = apartments1.pictured(state, True)
        t.write('number of elements, which have a picture = ' + str(k[0])+' ' +str(k[1])+ '%\n')
        k = apartments1.mapped(state,True)
        t.write('number of elements, which have a map = '+str(k[0])+' ' +str(k[1])+ '%\n')
        t.write(' *' * 20 + '\n')
        try:
            k = job1.number(state)
            t.write('number of jobs advertisments = '+ str(k)+ '\n')
        except:
            print(k)
            pass
        try:
            t.write('* ' * 20 + '\n')
            t.write('number of cars advertisments = ' + str(car1.number(state))+ '\n')

            t.write('average price = ' + str(car1.average_price(state))+ '\n')
            t.write('middle price = ' + str(car1.middle_price(state)) + '\n')
            t.write('average length of advertisment = ' + str(car1.average_len_advert(state)) + '\n')

            try:
                k = car1.most_popular_place(state, True)
                t.write('the most popular place = ' + str(k[0])+' ' +str(k[1])+ '%\n')
            except UnicodeEncodeError:
                t.write("the most popular place is secret, "+ str(k[1]) + '%\n')
            k = car1.geotaged(state, True)
            t.write('number geotagged = ' + str(k[0])+' ' +str(k[1])+ '%\n')
            k = car1.pictured(state, True)
            t.write('number of elements, which have a picture = ' + str(k[0])+' ' +str(k[1])+ '%\n')
            k = car1.mapped(state,True)
            t.write('number of elements, which have a map = '+str(k[0])+' ' +str(k[1])+ '%\n')
        except:
            #print(k)
            pass

        t.write('*' * 40 + '\n\n')
        print('proceeded data for ', state)
