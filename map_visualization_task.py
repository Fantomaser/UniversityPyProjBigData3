import Helper
import folium
from folium.plugins import MarkerCluster
import webbrowser
import os
import numpy as np
import matplotlib.pyplot as plt

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

        os.mkdir(".\\temp")

        map.save(".\\temp\\map2.html")
        
        webbrowser.open('.\\temp\\map2.html', new=1)

        labels = ["ЦАО", "Дмитровский район"]
        persents = [
            len(CAO)/((len(DR)+len(CAO))/100),
            len(DR)/((len(DR)+len(CAO))/100)
            ]

        explode = (0.1, 0)

        self.fig, self.ax = plt.subplots(figsize=(8,6))

        self.ax.pie(persents, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=350)
        self.ax.axis('equal')

        plt.show()

    def SwupCoordinates(self, coordinates):
        return [coordinates[1],coordinates[0]]

    def deleteTempFolder(self):
        if os.path.exists("temp"):
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp')
            shutil.rmtree(path)

    def close(self, json_container):
        plt.close(self.fig)
        self.deleteTempFolder()