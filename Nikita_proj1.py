from collections import Counter
import Helper
import json
import os
import shutil
import csv
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster


class Nikita_proj1:


    def open(self, json_container):
        fieldnames=["Район", "Количество камер"]
        fieldnames1=["Округ", "Количество камер"]
        cameraInfo=Helper.JsonList(json_container)
        district = cameraInfo.GetAllUniquWalue("District")
        admArea=cameraInfo.GetAllUniquWalue("AdmArea")
        count_district=cameraInfo.GetEqualRowsCount("District", district, fieldnames)
        count_admArea=cameraInfo.GetEqualRowsCount("AdmArea", admArea, fieldnames1)
        #Создание csv файла  данными count_district
        self.csv_dict_writer(path = ".\\temp\\dict_output.csv", fieldnames = ["Район", "Количество камер"], data=count_district)
        #Создание csv файла с данными count_admArea
        #self.csv_dict_writer(path=  ".\\temp\\admArea_output.csv", fieldnames=["Округ", "Количество камер"], data=count_admArea)



#Запись данных в csv файл:
    def csv_dict_writer(self, path, fieldnames, data):

        os.mkdir(".\\temp")

        with open(path, "w", newline='') as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
            writer.writeheader()
            for row in data.GetList():
                print(row)
                writer.writerow(row)

        #Визуализация данных
        df = pd.read_csv('.\\temp\dict_output.csv', encoding='windows-1251')

        df.plot.bar(x='Район', y='Количество камер', cmap='coolwarm')
        plt.show()


    def close(self, json_container):
        self.DeleteTempFolder()