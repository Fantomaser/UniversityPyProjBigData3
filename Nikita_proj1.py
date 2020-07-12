#author Арзаняев Никита

from collections import Counter
import Helper
import shutil
import csv
import os

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl

import seaborn as sns

from folium.plugins import MarkerCluster
import folium

class Nikita_proj1:
    def open(self, json_container):
        try:
            self.pathRayon = ".\\temp\\dict_output.csv"
            self.pathArea = ".\\temp\\admArea_output.csv"

            fieldnames=["Район", "Количество камер"]
            fieldnames1=["Округ", "Количество камер"]
            cameraInfo=Helper.JsonList(json_container)
            district = cameraInfo.GetAllUniquWalue("District")
            admArea = cameraInfo.GetAllUniquWalue("AdmArea")
            count_district=cameraInfo.GetEqualRowsCount("District", district, fieldnames)
            count_admArea=cameraInfo.GetEqualRowsCount("AdmArea", admArea, fieldnames1)

            os.mkdir(".\\temp")

                #Создание csv файла  данными count_district
            self.csv_dict_writer(path = self.pathRayon, fieldnames = ["Район", "Количество камер"], data=count_district)
                #Создание csv файла с данными count_admArea
            print(count_admArea)
            self.csv_dict_writer(path = self.pathArea, fieldnames = ["Округ", "Количество камер"], data=count_admArea)


                #Визуализация данных
            df = pd.read_csv(self.pathRayon, encoding='windows-1251')

            df.plot.bar(x='Район', y='Количество камер', cmap='coolwarm')
            plt.show()
        except:
            self.DeleteTempFolder()


    #Запись данных в csv файл:
    def csv_dict_writer(self, path, fieldnames, data):

        with open(path, "w", newline='') as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
            writer.writeheader()
            for row in data.GetList():
                print(row)
                writer.writerow(row)

    def DeleteTempFolder(self):
        if os.path.exists("temp"):
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp')
            shutil.rmtree(path)

    def close(self, json_container):
        self.DeleteTempFolder()