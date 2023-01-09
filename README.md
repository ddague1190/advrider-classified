# motorcycle-app_BE1

scraped from motoryccle database to use for a form for entering motorcycle model


mfgs_of_interest = [
        'bmw', 
        'ducati',
        'ktm',
        'moto_guzzi',
        'triumph',
        'harley-davidson',
        'kawasaki',
        'honda', 
        'yamaha',
        'beta',
        'aprilia',
        'suzuki',
        'husqvarna',
        'ural',
        'indian'
  ]

ENDPOINT https://motorcycle-models-api.herokuapp.com/api/

will pull all models made in the year queried:
api/?year=2000 bikes made in year 2000 

add a manufactuer from list above but it is 1 indexed (1='bmw')
api/?year=2006&mfg=2 made in year 2006 by ducati

results:
[
    {
        "id": 522,
        "start_year": 2003,
        "end_year": 2006,
        "model": "Ducati 749",
        "mfg": 2
    },
    {
        "id": 523,
        "start_year": 2004,
        "end_year": 2006,
        "model": "Ducati 749 R",
        "mfg": 2
    },
    {
        "id": 560,
        "start_year": 2003,
        "end_year": 2006,
        "model": "Ducati 749 S",
        "mfg": 2
    },
    {
        "id": 979,
        "start_year": 2003,
        "end_year": 2006,
        "model": "Ducati 999",
        "mfg": 2
    },
    {
        "id": 1124,
        "start_year": 2006,
        "end_year": 2006,
        "model": "Ducati HM Hypermotard",
        "mfg": 2
    },
    {
        "id": 1292,
        "start_year": 2003,
        "end_year": 2008,
        "model": "Ducati Monster 1000",
        "mfg": 2
    },
    {
        "id": 1325,
        "start_year": 2002,
        "end_year": 2006,
        "model": "Ducati Monster 620",
        "mfg": 2
    },
    {
        "id": 1473,
        "start_year": 2005,
        "end_year": 2015,
        "model": "Ducati Monster S2R",
        "mfg": 2
    },
    {
        "id": 1475,
        "start_year": 2003,
        "end_year": 2008,
        "model": "Ducati Monster S4R",
        "mfg": 2
    },
    {
        "id": 1495,
        "start_year": 2002,
        "end_year": 2006,
        "model": "Ducati Multistrada 1000",
        "mfg": 2
    },
    {
        "id": 1518,
        "start_year": 2005,
        "end_year": 2019,
        "model": "Ducati Multistrada 620",
        "mfg": 2
    },
    {
        "id": 1725,
        "start_year": 2006,
        "end_year": 2010,
        "model": "Ducati SportClassic",
        "mfg": 2
    },
    {
        "id": 1758,
        "start_year": 2004,
        "end_year": 2007,
        "model": "Ducati ST 3",
        "mfg": 2
    },
    {
        "id": 1800,
        "start_year": 2006,
        "end_year": 2006,
        "model": "Ducati Superbike 999R Xerox",
        "mfg": 2
    },
    {
        "id": 1813,
        "start_year": 2003,
        "end_year": 2006,
        "model": "Ducati Supersport 1000",
        "mfg": 2
    }
]
