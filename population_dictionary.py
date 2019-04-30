import pandas as pd

raw_population = pd.read_excel('data/gapdata003 old 2011.xlsx', usecols=[0,1,3])

raw_population = raw_population[raw_population['Year'] > 1960]
raw_population.replace({'Antigua and Barbuda':'Antigua & Barbuda',
    'Bahamas, The':'Bahamas',
    'Cook Is': 'Cook Islands',
    "Cote d'Ivoire":"Cote d`Ivoire",
    'Congo, Dem. Rep.': 'Congo, Democratic Republic of',
    'Congo, Rep.':'Congo, Republic of',
    'Iran, Islamic Rep.': 'Iran',
    'Gambia, The':'Gambia',
    'Korea, Dem. Rep.': 'Korea, Democratic Republic of',
    'Bosnia and Herzegovina': 'Bosnia-Herzegovina',
    'Falkland Is (Malvinas)': 'Falkland Islands',
    'Micronesia, Fed. Sts.': 'Micronesia, Federated States of',
    'Trinidad and Tobago': 'Trinidad & Tobago',
    'Wallis et Futuna': 'Wallis & Futuna',
    'British Virgin Islands': 'Virgin Islands (UK)',
    'Egypt, Arab Rep.':'Egypt',
    'Vietnam': 'Viet Nam',
    'Lao PDR':'Laos',
    'Macao, China':'Macao',
    'Russian Federation':'Russia',
    'USSR':'Soviet Union',
    'Sao Tome and Principe':'Sao Tome & Principe',
    'St. Kitts and Nevis':'St. Kitts & Nevis',
    'Saint Helena':'St. Helena',
    'St. Vincent and the Grenadines':'St. Vincent & Grenadines',
    'Syrian Arab Republic':'Syria',
    'Saint-Pierre-et-Miquelon':'St. Pierre & Miquelon',
    'Venezuela, RB':'Venezuela',
    'Yemen Arab Republic (Former)':'Yemen',
    'Poland':'Poland'}, inplace=True)

raw_population.to_csv('gapminder_pop_matched_aid.csv')