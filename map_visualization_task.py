import Helper
import folium
from folium.plugins import MarkerCluster
import webbrowser

class MapVisualizationProjectEvgen:
    def open(self, json_container):
        cameraInfo = Helper.JsonList(json_container)
        pr = cameraInfo
        DR = cameraInfo.GetWereEqual("District", "Дмитровский район").GetList()
        CAO = cameraInfo.GetWereEqual("AdmArea", "Центральный административный округ").GetList()
        
        map = folium.Map(location=[55.753228, 37.622480], zoom_start = 9)

        marker_cluster_dr = MarkerCluster().add_to(map)

        for camera in DR:
            folium.CircleMarker(location=self.SwupCoordinates(camera["geoData"]["coordinates"]), radius = 8, fill_color="red", color="gray", popup = camera["Address"], fill_opacity = 0.9).add_to(marker_cluster_dr)

        marker_cluster_cao = MarkerCluster().add_to(map)

        
        for camera in CAO:
            folium.CircleMarker(location=self.SwupCoordinates(camera["geoData"]["coordinates"]), radius = 8, fill_color="red", color="gray", popup = camera["Address"], fill_opacity = 0.9).add_to(marker_cluster_cao)

        map.save("map.html")

        #m = folium.Map(location=[55.764414, 37.647859])
        #m.choropleth(
        #    geo_data=full_gdf[['okrug', 'geometry']].to_json(),
        #    name='choropleth',
        #    data=full_gdf[['okrug', 'voters_oa']],
        #    key_on='feature.properties.okrug',
        #    columns=['okrug', 'voters_oa'],
        #    fill_color='YlGnBu',
        #    line_weight=1,
        #    fill_opacity=0.7,
        #    line_opacity=0.2,
        #    legend_name='type',
        #    highlight = True
        #)
        #m.save("map.html")
        
        webbrowser.open('.\map.html', new=1)

    def SwupCoordinates(self, coordinates):
        return [coordinates[1],coordinates[0]]

    def close(self, json_container):
        print("")