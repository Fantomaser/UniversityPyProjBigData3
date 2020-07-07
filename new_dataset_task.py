import os
import zipfile
import requests
import json
import shutil
import matplotlib.pyplot as plt
import numpy as np

class JsonList(list):
    def __init__(self, collection):
        self.collection = collection

    def GetAllUniquWalue(self, param_name):
        qnique_collection = list()
        for it in self.collection:
            val = it.get(param_name)
            if val != None and qnique_collection.count(val) == 0:
                qnique_collection.append(val)
        return qnique_collection

    def Count(self):
        return len(self.collection)
    
    def GetEqualRowsCount(self, param_name, collection):
        n_collection = list()
        counter = 0
        for it in collection:           
            for it2 in self.collection:
                val = it2.get(param_name)
                if val != None:
                    if type(val) == type([]):
                        if val[0] == it:
                            counter+=1
                    elif val == it:
                        counter+=1
            n_collection.append([it, counter])
            counter = 0
        return JsonList(n_collection)

    def ZipFilds(self, collection, name_1, name_2, name_3):
        n_collection = list()
        for it in self.collection:
            for it2 in collection.collection:
                if it[0] == it2[0]:
                    n_collection.append({name_1:it[0], name_2:it[1], name_3:it2[1]})
                    break
        return JsonList(n_collection)

    def MakeData(self):
        data = list()
        data.append([])
        data.append([])
        data.append([])
        for it in self.collection:
            data[0].append(it['Административный округ'])
            data[1].append(it['Камеры'])
            data[2].append(it['Участковый'])
        return data

    def __str__(self):
        return self.collection.__str__()

class ProjectEvgen:
    def open(self, json_container):
        
        cameraInfo = JsonList(json_container)

        #print(json_container)
        #print(cameraInfo)

        response = requests.get("https://op.mos.ru/EHDWSREST/catalog/export/get?id=867249")
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

        policeInfo = JsonList(json.loads(f.read(), encoding='windows-1251'))

        f.close()

        if os.path.exists("temp"):
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp')
            shutil.rmtree(path)

        # основная часть********************

        uniqueStreet = cameraInfo.GetAllUniquWalue("AdmArea")
        cameraCounter = cameraInfo.GetEqualRowsCount("AdmArea", uniqueStreet)
        print(uniqueStreet)
        print("-----------------")
        policeCounter = policeInfo.GetEqualRowsCount("AdmArea", uniqueStreet)
        print(policeCounter)
        print("-----------------")

        ZipInfo = cameraCounter.ZipFilds(policeCounter, "Административный округ", "Камеры", "Участковый")
        print(ZipInfo)

        data = ZipInfo.MakeData()

        X = np.arange(len(data[0]))

        self.fig = plt.figure()
        ax = self.fig.add_axes([0,0,1,1])

        ax.bar(X + 0.00, data[1], color = 'b', width = 0.25)
        ax.bar(X + 0.25, data[2], color = 'r', width = 0.25)
        plt.show()

        #************************************
    
    def close(self, json_container):
        plt.close(self.fig)