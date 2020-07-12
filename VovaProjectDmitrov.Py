import webbrowser
import shutil
import os

from folium.plugins import MarkerCluster
import folium

import Helper

#authon: Войнов Владимир

class ProjectVovaDmotrov:
    def open(self, json_container):   
        cameraInfo = Helper.JsonList(json_container)    
        
        number = cameraInfo.GetEqualRowsCount("District", ["Дмитровский район"]).GetList()[0][1]

        dmitrov_camera = cameraInfo.GetWereEqual("District", "Дмитровский район").GetList()

        
        map = folium.Map(location=[55.888157, 37.531341], zoom_start = 12)


        marker_cluster_dr = MarkerCluster().add_to(map)

        for camera in dmitrov_camera:
            folium.CircleMarker(location=self.SwupCoordinates(camera["geoData"]["coordinates"]), radius = 8, fill_color="red", color="gray", popup = camera["Address"], fill_opacity = 0.9).add_to(marker_cluster_dr)

        try:
            os.mkdir(".\\temp")
            map.save(".\\temp\\map.html")

            webbrowser.open('.\\temp\\map.html', new=1)
        except:
             self.DeleteTempFolder()

    def SwupCoordinates(self, coordinates):
        return [coordinates[1],coordinates[0]]

    def DeleteTempFolder(self):
        if os.path.exists("temp"):
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp')
            shutil.rmtree(path)
    
    def close(self, json_container):
        self.DeleteTempFolder()
        print("")