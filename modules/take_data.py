from craigslist import CraigslistHousing, CraigslistJobs,  CraigslistEvents, CraigslistForSale

taken_sites = ['austin','dallas','sandiego','sanantonio','phoenix','philadelphia','houston','delaware','chicago',
               'losangeles','maine','montana','newyork', 'vermont',   'wyoming', 'denver','seattle','boston','memphis',
               'elpaso','detroit','charlotte','columbus','indianapolis','jacksonville','albuquerque','lasvegas',
               'milwaukee','oklahoma','portland','louisville','baltimore']
new_sites = ['tucson', 'fresno', 'sacramento',   'atlanta',
             'raleigh', 'omaha', 'miami', 'tulsa', 'minneapolis', 'cleveland', 'wichita',
             'neworleans', 'bakersfield']
'''
 'tampa', 'honolulu', 'anaheim', 'aurora', 'santaana', 'st.louis',
             'riverside', 'corpuschristi', 'pittsburgh', 'lexington-fayette', 'anchoragemunicipality', 'stockton',
             'cincinnati', 'st.paul', 'toledo', 'newark', 'greensboro', 'plano', 'henderson', 'lincoln', 'buffalo',
             'fortwayne', 'jersey', 'chulavista', 'orlando', 'st.petersburg', 'norfolk', 'chandler', 'laredo',
             'madison', 'durham', 'lubbock', 'winston-salem', 'garland', 'glendale', 'hialeah', 'reno', 'batonrouge',
             'irvine', 'chesapeake', 'irving', 'scottsdale', 'northlasvegas', 'fremont', 'gilberttown', 'sanbernardino',
             'boise', 'birmingham'
'''
# b =0 take data for houses, b = 1 take data for jobs, b = 2 take data for cars
b = 1
if b ==0:
    for name in new_sites:
        try:

            with open("term_project/catalog/data/DATA_by_date_"+name+".txt", 'w', encoding='utf-8') as d:
                cl_h = CraigslistHousing(site=name)

                #m = 0
                for result in cl_h.get_results(sort_by='newest'):
                    try:
                        d.write(str(result))
                        d.write('\n')
                        # just to see it works
                        print(1)
                        #m = result
                    except UnicodeEncodeError:
                        continue
                    except ConnectionError:
                        continue
        except ValueError:
            print(name)

elif b == 1:
    for name in new_sites:
        try:

            with open("term_project/catalog/data/DATA_by_jobs_" + name + ".txt", 'w', encoding='utf-8') as d:
                cl_j = CraigslistJobs(site=name)

                # m = 0
                for result in cl_j.get_results(sort_by='newest'):
                    try:
                        d.write(str(result))
                        d.write('\n')
                        # just to see it works
                        print(1)
                        # m = result
                    except UnicodeEncodeError:
                        continue
                    except ConnectionError:
                        continue
        except ValueError:
            print(name)

elif b == 2:
    for name in new_sites:
        try:

            with open("term_project/catalog/data/DATA_by_cars_" + name + ".txt", 'w', encoding='utf-8') as d:
                cl_fs = CraigslistForSale(site=name)

                # m = 0
                for result in cl_fs.get_results(sort_by='newest'):
                    try:
                        d.write(str(result))
                        d.write('\n')
                        # just to see it works
                        print(1)
                        # m = result
                    except UnicodeEncodeError:
                        continue
                    except ConnectionError:
                        continue
        except ValueError:
            print(name)



        '''
        for i in range(50):
            cl_h = CraigslistHousing(site=name, filters={'min_price': int(m['price'])[1:]})
            for result in cl_h.get_results(sort_by='price_asc' ):
                try:
                    d.write(str(result))
                    d.write('\n')
                    # just to see it works
                    #print(1)
                    m = result
                except UnicodeEncodeError:
                    continue
                except ConnectionError:
                    continue

        '''
