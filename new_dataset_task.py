#author: Соловьев Евгений

import requests
import zipfile
import shutil
import json
import os

import matplotlib.pyplot as plt
import numpy as np

import Helper

class NewDataProjectEvgen:
    def open(self, json_container):
        try:      
            cameraInfo = Helper.JsonList(json_container)

            hostelInfo = self.LoadNewInfo("https://op.mos.ru/EHDWSREST/catalog/export/get?id=840262")#гостиницы

            uniqueArea = cameraInfo.GetAllUniquWalue("AdmArea")
            cameraCounter = cameraInfo.GetEqualRowsCount("AdmArea", uniqueArea)
            hostelCounter = hostelInfo.GetEqualRowsCount("AdmArea", uniqueArea)

            ZipInfo = cameraCounter.ZipFilds(hostelCounter, "Административный округ", "Камеры", "Гостиницы")

            data = ZipInfo.MakePairComparisonData("Административный округ", "Камеры", "Гостиницы").GetList()

            X = np.arange(len(data[0]))

            self.fig, self.ax = plt.subplots(figsize=(8,6))
            self.fig.canvas.set_window_title('Сравнение количества камер и гостиниц')

            rects1 = self.ax.bar(X + 0.00, data[1], color = 'b', width = 0.40, label="камеры")
            rects2 = self.ax.bar(X + 0.40, data[2], color = 'r', width = 0.40, label="гостиницы")

            self.ax.set_ylabel('Scores')
            self.ax.set_title("Cameras vs Hotels")
            self.ax.set_xticks(X)
            self.ax.set_xticklabels(data[0])
            self.ax.legend()

            self.fig.tight_layout()

            plt.show()
        except:
            self.DeleteTempFolder()
            print("solov open data set")

    def LoadNewInfo(self, url):
        response = requests.get(url)

        if response.status_code != 200:
            print("Server Error")
        else:
            print("Server Ok state")

        response.encoding = 'windows-1251'
        
        os.mkdir(".\\temp")
        f = open('.\\temp\\n_responce.zip', 'wb')
        f.write(response.content)
        f.close()

        z = zipfile.ZipFile('.\\temp\\n_responce.zip', 'r')
        z.extractall(".\\temp")
        z.close()

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp\\n_responce.zip')
        os.remove(path)

        files = os.listdir(".\\temp")
        f = open('.\\temp\\'+files[0], 'r', encoding='windows-1251')

        info = Helper.JsonList(json.loads(f.read(), encoding='windows-1251'))

        f.close()

        return info

    def DeleteTempFolder(self):
        if os.path.exists("temp"):
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp')
            shutil.rmtree(path)
    
    def close(self, json_container):
        try:
            plt.close(self.fig)
        except:
            print("solov close data set")
        self.DeleteTempFolder()