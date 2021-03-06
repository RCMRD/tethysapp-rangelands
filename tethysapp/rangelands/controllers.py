import random
import string
import fnmatch

from django.shortcuts import render
from tethys_sdk.permissions import login_required

from tethys_sdk.gizmos import *
from .app import Rangelands as app
from .modis.datasets import *

WORKSPACE = 'rangelands'
GEOSERVER_URI = 'http://www.rcmrd.org/rangelands'

#@login_required()
def home(request):
    """
    Controller for the home page
    :param request:
    :return:
    """

    # latest dekadal wms
    geoserver_engine = app.get_spatial_dataset_service(name='main_geoserver', as_engine=True)
    dekadal_lyrs = []
    response = geoserver_engine.list_layers(with_properties=False)

    if response['success']:
        for layer in response['result']:
            layer_title = layer.title()
            if fnmatch.fnmatch(layer_title, '*Modis.Dekadal.2020*'):
                dekadal_lyrs.append(layer_title.lower())
    

    # dataset select
    indicator_select = SelectInput(
        name='indicator',
        display_text='Greeness Indicator',
        options=(
            ('NDVI', 'ndvi'),
            ('NDVI Anomaly', 'ndvi_anomaly'),
            ('Vegetation Condition Index', 'vci')
        )
    )

    # temporal select
    product_select = SelectInput(
        name='product',
        display_text='Product',
        options=(
            ('Near Real Time(10 days)', 'dekadal'),
            ('Monthly', 'monthly'),
            ('Seasonal', 'seasonal')

        )
    )

    year_options = []
    for y in years:
        year_options.append((y, y))

    # year select
    year_select = SelectInput(
        name='year',
        display_text='Year',
        options=year_options
    )

    season_options = []
    for s in seasons:
        season_options.append((s['label'], s['value']))
    # season select
    season_select = SelectInput(
        name='season',
        display_text='Season',
        options=season_options
    )

    month_options = []
    for m in months:
        i = str(months.index(m) + 1)
        if len(i) > 1:
            v = i
        else:
            v = '0' + i
        month_options.append((m, v))

    # year select
    month_select = SelectInput(
        name='month',
        display_text='Month',
        options=month_options
    )

    # year select
    dekad_options = []
    for dekad in dekads:
        dekad_options.append((dekad['label'], dekad['value']))

    dekad_select = SelectInput(
        name='dekad',
        display_text='Dekad',
        options=dekad_options
    )

    # Buttons
    load_button = Button(
        name='load_map',
        display_text='Load',
        style='default',
        attributes={'id': 'load_map'}
    )

    compose_button = Button(
        name='compose_map',
        display_text='Compose Map',
        style='default',
        attributes={'id': 'compose_map'}
    )



    map_layers = []

    latest_layer = 'rangelands:modis.dekadal.20200721.tif'
    legend_title = 'modis.dekadal.20200721.tif'
    geoserver_layer = MVLayer(
        source='ImageWMS',
        options={
            'url': 'http://apps.rcmrd.org:8080/geoserver/wms',
            'params': {'LAYERS': latest_layer},
            'serverType': 'geoserver'
        },
        legend_title=legend_title,
    )
    map_layers.append(geoserver_layer)

    view_options = MVView(
        projection='EPSG:4326',
        center=[37.880859, 0.219726],
        zoom=7,
        maxZoom=18,
        minZoom=2
    )

    map_options = MapView(
        height='100%',
        width='100%',
        controls=[
            'ZoomSlider', 'Rotate', 'FullScreen',
            {'ZoomToExtent': {
                'projection': 'EPSG:4326',
                'extent': [29.25, -4.75, 46.25, 5.2]  #: Kenya
            }}
        ],
        #layers=map_layers,
        #legend=True,
        view=view_options
    )

    context = {
        'map_options': map_options,
        #'select_options': select_options,
        'indicator_select': indicator_select,
        'product_select': product_select,
        'year_select': year_select,
        'season_select': season_select,
        'month_select': month_select,
        'dekad_select': dekad_select,
        'load_button': load_button,
        'compose_button': compose_button,
        'latest_dekadal': max(dekadal_lyrs),
        'rdst_datasets': DATASETS
    }

    return render(request, 'rangelands/map.html', context)