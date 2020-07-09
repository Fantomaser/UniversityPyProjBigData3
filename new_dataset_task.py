import os
import zipfile
import requests
import json
import shutil
import matplotlib.pyplot as plt
import numpy as np
import Helper

class NewDataProjectEvgen:
    def open(self, json_container):
        
        cameraInfo = Helper.JsonList(json_container)

        response = requests.get("https://op.mos.ru/EHDWSREST/catalog/export/get?id=840262")#гостиницы
        #https://op.mos.ru/EHDWSREST/catalog/export/get?id=851697 #участковый
        #https://op.mos.ru/EHDWSREST/catalog/export/get?id=788381 #жратва
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

        policeInfo = Helper.JsonList(json.loads(f.read(), encoding='windows-1251'))

        f.close()

        if os.path.exists("temp"):
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp')
            shutil.rmtree(path)

        # основная часть********************

        uniqueArea = cameraInfo.GetAllUniquWalue("AdmArea")
        cameraCounter = cameraInfo.GetEqualRowsCount("AdmArea", uniqueArea)
        policeCounter = policeInfo.GetEqualRowsCount("AdmArea", uniqueArea)

        ZipInfo = cameraCounter.ZipFilds(policeCounter, "Административный округ", "Камеры", "Гостиницы")
        print(ZipInfo)

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

        #************************************
    
    def close(self, json_container):
        plt.close(self.fig)