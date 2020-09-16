from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import SpatialDatasetServiceSetting


class Rangelands(TethysAppBase):
    """
    Tethys app class for Rangelands Decision Support Tool.
    """

    name = 'Rangelands Decision Support Tool'
    index = 'rangelands:home'
    icon = 'rangelands/images/icon.gif'
    package = 'rangelands'
    root_url = 'rangelands'
    color = '#f39c12'
    description = 'Rangelands Decision Support Tool'
    tags = '"Rangelands"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='rangelands',
                controller='rangelands.controllers.home'
            ),
        )

        return url_maps


    def spatial_dataset_service_settings(self):
        """
        Example spatial_dataset_service_settings method.
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name='main_geoserver',
                description='spatial dataset service for app to use',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
        )

        return sds_settings