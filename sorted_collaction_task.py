import Helper
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
import os
import pickle

class SortedCollactionProjectEvgen:
    def open(self, json_container):
        cameraInfo = Helper.JsonList(json_container)

        uniqueArea = cameraInfo.GetAllUniquWalue("AdmArea")
        cameraCounter = cameraInfo.GetEqualRowsCount("AdmArea", uniqueArea)

        sortedCameraCounter = Helper.JsonList(sorted(cameraCounter.GetList(), key=lambda camera: camera[1]))

        data = sortedCameraCounter.MakeComparisonData().GetList()

        print(data)

        X = np.arange(len(data[0]))

        self.fig, self.ax = plt.subplots(figsize=(8,6))
        self.fig.canvas.set_window_title('Проверка суждения о количестве камер в районах ЦАО')

        rects = self.ax.bar(X + 0.00, data[1], color = 'b', width = 0.50, label="камеры")

        self.ax.set_ylabel('Scores')
        self.ax.set_title("Количество камер по округам")
        self.ax.set_xticks(X)
        self.ax.set_xticklabels(data[0])
        self.ax.legend()

        self.autolabel(rects, "left")

        self.fig.tight_layout()

        plt.show()

    def autolabel(self, rects, xpos='center'):
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0, 'right': 1, 'left': -1}

        for rect in rects:
            height = rect.get_height()
            self.ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(offset[xpos]*3, 3),  # use 3 points offset
                        textcoords="offset points",  # in both directions
                        ha=ha[xpos], va='bottom')

    def close(self, json_container):
        plt.close(self.fig)