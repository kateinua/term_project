with open('states.txt', 'r') as f:
    el = f.readline()
    sites = []
    while el is not None and el != '':
        el = el.replace(' ','')
        el = el.replace('\n', '')
        sites.append(el.lower())
        el = f.readline()
        #print(el)
print(sites)

stat = ['newyork', 'losangeles', 'chicago', 'houston', 'philadelphia', 'phoenix', 'sanantonio', 'sandiego', 'dallas',
        'sanjose', 'austin', 'jacksonville', 'indianapolis', 'columbus', 'charlotte', 'detroit', 'elpaso', 'memphis',
        'boston', 'seattle', 'denver', 'baltimore', 'louisville', 'portland', 'milwaukee', 'lasvegas', 'albuquerque',
        'tucson', 'fresno', 'sacramento', 'longbeach', 'kansas', 'mesa', 'virginiabeach', 'atlanta', 'coloradosprings',
        'raleigh', 'omaha', 'miami', 'oakland', 'tulsa', 'minneapolis', 'cleveland', 'wichita', 'arlington',
        'neworleans', 'bakersfield', 'tampa', 'honolulu', 'anaheim', 'aurora', 'santaana', 'st.louis', 'riverside',
        'corpuschristi', 'pittsburgh', 'lexington-fayette', 'anchoragemunicipality', 'stockton', 'cincinnati',
        'st.paul', 'toledo', 'newark', 'greensboro', 'plano', 'henderson', 'lincoln', 'buffalo', 'fortwayne', 'jersey',
        'chulavista', 'orlando', 'st.petersburg', 'norfolk', 'chandler', 'laredo', 'madison', 'durham', 'lubbock',
        'winston-salem', 'garland', 'glendale', 'hialeah', 'reno', 'batonrouge', 'irvine', 'chesapeake', 'irving',
        'scottsdale', 'northlasvegas', 'fremont', 'gilberttown', 'sanbernardino', 'boise', 'birmingham']

taken_sites = ['austin','dallas','sandiego','sanantonio','phoenix','philadelphia','houston','delaware','chicago',
               'losangeles','maine','montana','newyork', 'vermont',   'wyoming', 'denver','seattle','boston','memphis',
               'elpaso','detroit','charlotte','columbus','indianapolis','jacksonville','albuquerque','lasvegas',
               'milwaukee','oklahoma','portland','louisville','baltimore']
for el in taken_sites:
    if el in stat:
        stat.remove(el)

print(stat)