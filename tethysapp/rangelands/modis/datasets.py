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
    'value': 'season1'
},{
    'label': 'Oct-Nov-Dec',
    'value': 'season2'
}
]

DATASETS = {
    'ndvi':{
        'display': 'Normalized Difference Vegetation Index',
        'products': {
            'dekadal':{
                        'display': 'Near Real Time (10-days)',
                        'description': '',
                        'options': {
                            'year': {
                                'display': 'Year',
                                'list': years
                            },
                            'month':{
                                'display': 'Month',
                                'list': months
                            },
                            'decad':{
                                'display': 'Decad',
                                'list': dekads
                            }
                        }
                    },
                    'monthly': {
                        'display': 'Monthly',
                        'description': '',
                        'options': {
                            'year': {
                                'display': 'Year',
                                'list': years
                            },
                            'month': {
                                'display': 'Month',
                                'list': months
                            }
                        }
                    },
                    'seasonal': {
                        'display': 'Seasonal',
                        'description': '',
                        'options': {
                            'year': {
                                'display': 'Year',
                                'list': years
                            },
                            'season': {
                                'display': 'Season',
                                'list': seasons
                            }
                        }
                    }
        }

    },
    'ndvi_anomaly': {
        'display':'NDVI Anomaly',
        'products':{
            'std_monthly':{
                        'display': 'STD Monthly',
                        'description': '',
                        'options': {
                                        'year': {
                                            'display': 'Year',
                                            'list': years
                                        },
                                        'month': {
                                            'display': 'Month',
                                            'list': months
                                        }
                                    }

                    },
                    'std_seasonal':{
                        'display': 'STD Seasonal',
                        'description': '',
                        'options': {
                                        'year': {
                                            'display': 'Year',
                                            'list': years
                                        },
                                        'season': {
                                            'display': 'Season',
                                            'list': seasons
                                        }
                                    }

                    },
                    'abs_monthly':{
                        'display': 'ABS Monthly',
                        'description': '',
                        'options': {
                                        'year': {
                                            'display': 'Year',
                                            'list': years
                                        },
                                        'month': {
                                            'display': 'Month',
                                            'list': months
                                        }
                                    }

                    },
                    'abs_seasonal':{
                        'display': 'ABS Seasonal',
                        'description': '',
                        'options': {
                                        'year': {
                                            'display': 'Year',
                                            'list': years
                                        },
                                        'season': {
                                            'display': 'Season',
                                            'list': seasons
                                        }
                                    }

                    }
        }


    },
    'vci':{
        'display': 'Vegetation Condition Index',
        'products':{
            'vci_monthly':{
                        'display': 'VCI Monthly',
                        'description': '',
                        'options': {
                                        'year': {
                                            'display': 'Year',
                                            'list': years
                                        },
                                        'month': {
                                            'display': 'Month',
                                            'list': months
                                        }
                                    }
                    },
                    'vci_seasonal':{
                        'display': 'VCI Seasonal',
                        'description': '',
                        'options': {
                                        'year': {
                                            'display': 'Year',
                                            'list': years
                                        },
                                        'season': {
                                            'display': 'Season',
                                            'list': seasons
                                        }
                                    }

                    }
        }


    }
}