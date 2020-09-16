var DATASETS = (function(){
    // wrap the library in a package function
    "use strict"; // enable strict mode for this library

    /*
    MODULE LEVEL / GLOBAL VARIABLES
    */

    var RDST_DATASETS;

    var public_interface;

    // Selector variables
    var m_indicator,
        m_product,
        m_year,
        m_season,
        m_month,
        m_dekad;

    // Map variables
    var map, new_layer;

    /*
    PRIVATE FUNCTION DECLARATIONS
    */
    // Dataset Select Methods
    var bind_controls, update_product_options, update_temporal_options, collect_data;

    /*
    PRIVATE FUNCTION IMPLEMENTATIONS
    */
    // Dataset Select Methods
    bind_controls = function(){
        $('#indicator').on('change', function(){
            let indicator = $('#indicator').val();
            if(indicator !== m_indicator){
                m_indicator = indicator;
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


    };

    update_product_options = function(){
        // Clear product options
        $('#product').select2().empty();

        // Set product options
        let first_option = true;
        for(var product in RDST_DATASETS[m_indicator]['products']){
            let product_display_name = RDST_DATASETS[m_indicator]['products'][product]['display'];
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

        new_layer = new ImageLayer({
            source: new ImageWMS({
                url: 'http://apps.rcmrd.org:8080/geoserver/wms',
                params: {'LAYERS': 'rangelands:Kenya_Range_Counties'},
                serverType: 'geoserver',
                crossOrigin: 'anonymous'
            })
        });

        map.addLayer(new_layer);



    });

    return public_interface;


}()); // End of package wrapper