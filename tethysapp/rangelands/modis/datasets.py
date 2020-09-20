"""
MODIS NDVI Datasets
"""
import datetime
import calendar

# dataset lists
year = datetime.datetime.today().year
years = [year - i for i in range(20)]

months = []
for i in range(1,13):
    months.append(calendar.month_name[i])

dekads = [{
    'label': 'Dekad 1 (1st - 10th)',
    'value': '01'
},{
    'label': 'Dekad 2 (11th - 20th)',
    'value': '11'
},{
    'label': 'Dekad 3 (21st - 30th)',
    'value': '21'
}]

seasons = [{
    'label': 'Mar-Apr-May',
    'value': '01'
},{
    'label': 'Oct-Nov-Dec',
    'value': '02'
}
]

DATASETS = {
    'ndvi':{
        'display': 'Normalized Difference Vegetation Index',
        'products': {
            'dekadal':{
                        'display': 'Near Real Time (10-days)',
                        'description': ''
                    },
                    'monthly': {
                        'display': 'Monthly',
                        'description': ''
                    },
                    'seasonal': {
                        'display': 'Seasonal',
                        'description': ''
                    }
        }

    },
    'ndvi_anomaly': {
        'display':'NDVI Anomaly',
        'products':{
            'std_monthly':{
                        'display': 'STD Monthly',
                        'value': 'SA',
                        'description': ''

                    },
                    'std_seasonal':{
                        'display': 'STD Seasonal',
                        'value': 'SA',
                        'description': ''

                    },
                    'abs_monthly':{
                        'display': 'ABS Monthly',
                        'value': 'AA',
                        'description': ''

                    },
                    'abs_seasonal':{
                        'display': 'ABS Seasonal',
                        'value': 'SA',
                        'description': ''

                    }
        }


    },
    'vci':{
        'display': 'Vegetation Condition Index',
        'products':{
            'vci_monthly':{
                        'display': 'VCI Monthly',
                        'value': 'VCI',
                        'description': ''
                    },
                    'vci_seasonal':{
                        'display': 'VCI Seasonal',
                        'value': 'VCI',
                        'description': ''

                    }
        }


    }
}