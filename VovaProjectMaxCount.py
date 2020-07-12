import matplotlib.pyplot as plt

import Helper

#authon: Войнов Владимир

class VovaProjectMaxCount:
    def open(self, json_container):
        try:
            cameraInfo = Helper.JsonList(json_container)    
            uniqueArea = cameraInfo.GetAllUniquWalue("AdmArea") 
            cameraCounter = cameraInfo.GetEqualRowsCount("AdmArea", uniqueArea)

            sortedCamera = sorted(cameraCounter.GetList(), key=lambda camera: camera[1])

            data = Helper.JsonList(sortedCamera).MakeComparisonData().GetList()

            explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1)

            self.fig, ax = plt.subplots(figsize=(8,6))

            ax.pie(data[1], explode=explode, labels=data[0], autopct='%1.1f%%', shadow=False, startangle=30)
            ax.axis('equal')

            plt.show()
        except:
            print("error open vova proj max count")

    def close(self, json_container):
        try:
            plt.close(self.fig)
        except:
            print("error close vova proj max count")