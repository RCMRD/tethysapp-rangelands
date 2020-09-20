var DATASETS = (function(){
    // wrap the library in a package function
    "use strict"; // enable strict mode for this library

    /*
    MODULE LEVEL / GLOBAL VARIABLES
    */

    var RDST_DATASETS, latest_dekadal;

    var public_interface;

    // Selector variables
    var m_indicator,
        m_product,
        m_year,
        m_season,
        m_month,
        m_dekad;

    // Map variables
    var map, wms_layer, selected_layer_name, current_layer_name ;

    /*
    PRIVATE FUNCTION DECLARATIONS
    */
    // Dataset Select Methods
    var bind_controls,
        load_dekadal_map,
        load_monthly_map,
        load_seasonal_map,
        add_wms_layer,
        update_product_options,
        update_temporal_options,
        collect_data;

    /*
    PRIVATE FUNCTION IMPLEMENTATIONS
    */
    // Dataset Select Methods
    bind_controls = function(){
        $('#indicator').on('change', function(){
            let indicator = $('#indicator').val();
            if(indicator !== m_indicator){
                m_indicator = indicator;
                //console.log(m_indicator);
                update_product_options();
            }

        });

        $('#product').on('change', function(){
            let product = $('#product').val();
            if(product !== m_product){
                m_product = product;
                update_temporal_options();
            }
        });

        $('#year').on('change', function(){
            let year = $('#year').val();
            if(year !== m_year){
                m_year = year;
            }
        });

        $('#month').on('change', function(){
            let month = $('#month').val();
            if(month !== m_month){
                m_month = month;

                if(m_product.includes("monthly")){
                    load_monthly_map();
                }

            }
        });

        $('#season').on('change', function(){
            let season = $('#season').val();
            if(season !== m_season){
                m_season = season;

                if(m_product.includes("seasonal")){
                    load_seasonal_map();
                }

            }

        });

        $('#dekad').on('change', function(){
            let dekad = $('#dekad').val();
            if(dekad !== m_dekad){
                m_dekad = dekad;
                load_dekadal_map();
            }
        });


    };

    load_dekadal_map = function(){

        // clear current map overlay
        map.removeLayer(wms_layer);
        // generate layer name
        selected_layer_name = 'rangelands:modis.' + m_product + '.' + m_year + m_month + m_dekad + '.tif';
        //console.log(selected_layer_name);

        // add layer
        add_wms_layer();

    };


    load_monthly_map = function(){

        // clear current map overlay
        map.removeLayer(wms_layer);
        // generate layer name
        if(m_indicator == 'ndvi'){
            selected_layer_name = 'rangelands:modis.' + m_product + '.' + m_year + m_month + '.tif';
        } else if (m_indicator == 'ndvi_anomaly'){
            if(m_product == 'std_monthly'){
                selected_layer_name = 'rangelands:modis.monthly.SA.' + m_year + m_month + '.tif';
            } else {
                selected_layer_name = 'rangelands:modis.monthly.AA.' + m_year + m_month + '.tif';
            }

        } else {
            selected_layer_name = 'rangelands:modis.monthly.VCI.' + m_year + m_month + '.tif';
        }

        //console.log(selected_layer_name);
        // add layer
        add_wms_layer();

    }


    load_seasonal_map = function(){

        // clear current map overlay
        map.removeLayer(wms_layer);
        // generate layer name
        if(m_indicator == 'ndvi'){
            selected_layer_name = 'rangelands:modis.' + m_product + '.' + m_year + m_season + '.tif';
        } else if (m_indicator == 'ndvi_anomaly'){
            if(m_product == 'std_seasonal'){
                selected_layer_name = 'rangelands:modis.seasonal.SA.' + m_year + m_season + '.tif';
            } else {
                selected_layer_name = 'rangelands:modis.seasonal.AA.' + m_year + m_season + '.tif';
            }

        } else {
            selected_layer_name = 'rangelands:modis.seasonal.VCI.' + m_year + m_season + '.tif';
        }

        //console.log(selected_layer_name);
        // add layer
        add_wms_layer();

    }

    add_wms_layer = function(){
        wms_layer = new ol.layer.Image({
            source: new ol.source.ImageWMS({
                url: 'http://apps.rcmrd.org:8080/geoserver/wms',
                params: {'LAYERS': selected_layer_name},
                serverType: 'geoserver',
                crossOrigin: 'null'
            })
        });

        map.addLayer(wms_layer);
    }


    update_product_options = function(){
        // Clear product options
        $('#product').select2().empty();

        // Set product options
        let first_option = true;
        for(var product in RDST_DATASETS[m_indicator]['products']){
            let product_display_name = RDST_DATASETS[m_indicator]['products'][product]['display'];
            //let product_value = RDST_DATASETS[m_indicator]['products'][product]['value'];
            let new_option = new Option(product_display_name, product, first_option, first_option);
            $('#product').append(new_option);
            first_option = false;
        }

        // Trigger a product change event to update select box
        $('#product').trigger('change');

    };


    update_temporal_options = function(){
        // show/hide season, month, dekad selects
        if(m_product.includes("monthly")){
            $('#season_div').hide();
            $('#dekad_div').hide();
            $('#month_div').show();
        } else if(m_product.includes("seasonal")){
            $('#month_div').hide();
            $('#dekad_div').hide();
            $('#season_div').show();
        } else {
            $('#season_div').hide();
            $('#month_div').show();
            $('#dekad_div').show();
        }
    };

    collect_data = function(){};

    /*
    PUBLIC INTERFACE
    */
    public_interface = {};

    /*
    INITIALIZATION / CONSTRUCTOR
    */
    $(function(){
        // Initialize Global Variables
        bind_controls();

        // Initialize Constants
        RDST_DATASETS = $('#rdst-datasets').data('rdst-datasets');
        latest_dekadal = $('#latest-dekadal').data('latest-dekadal');

        current_layer_name = latest_dekadal;

        // Initialize members
        m_indicator = $('#indicator').val();
        m_product = $('#product').val();
        m_year = $('#year').val();
        m_month = $('#month').val();
        m_dekad = $('#dekad').val();
        m_season = $('#season').val();

        // Hide selects
        $('#season_div').hide();

        // OL Map Object
        map = TETHYS_MAP_VIEW.getMap();

        wms_layer = new ol.layer.Image({
            source: new ol.source.ImageWMS({
                url: 'http://apps.rcmrd.org:8080/geoserver/wms',
                params: {'LAYERS': latest_dekadal},
                serverType: 'geoserver',
                crossOrigin: 'null'
            })
        });

        map.addLayer(wms_layer);




    });

    return public_interface;


}()); // End of package wrapper