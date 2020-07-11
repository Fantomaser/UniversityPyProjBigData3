import os
import zipfile
import requests
import json
import shutil
import tkinter 
import Helper
class ProjectVova:
    def open(self, json_container):
    
    cameraInfo = Helper.JsonList(json_container)
    
    uniqueArea = cameraInfo.GetAllUniquWalue("AdmArea")
    
    cameraCounter = cameraInfo.GetEqualRowsCount("AdmArea", uniqueArea)
    
    sortedCamera = sorted(cameraCounter.GetList(), key=lambda camera: camera[1])
    
    data = Helper.JsonList(sortedCameraCounter).MakeComparisonData().GetList()
    
    number = cameraInfo.GetEqualRowsCount("District", ["Дмитровский район"]).GetList()[0][1]

    print(number)
    
    number = cameraInfo.GetEqualRowsCount("District", ["Дмитровский район"]).Count()

    print(number)
    
    def close(self, json_container):