#author Арзаняев Никита

import json
import Helper
import os
import shutil

class ValueCounter:
    def open(self, json_container):
        cameraInfo=Helper.JsonList(json_container)

        district = cameraInfo.GetAllUniquWalue("District")
        admArea = cameraInfo.GetAllUniquWalue("AdmArea")

        count_district = cameraInfo.GetEqualRowsCount("District", district)
        count_admArea = cameraInfo.GetEqualRowsCount("AdmArea", admArea)

        json_add_district = self.AddDataByEqualRow(json_container, count_district.GetList(), "District", "eq_district_count")
        json_add_area = self.AddDataByEqualRow(json_add_district, count_admArea.GetList(), "AdmArea", "eq_area_count")

        self.ClearRes()

        os.mkdir(".\\res")

        with open(".\\res\\new_data.json", "w", newline='', encoding='windows-1251') as write_file:
            json.dump(json_add_area, write_file, ensure_ascii=False)
        


    def AddDataByEqualRow(self, container, addData, eqFild, newfildName):
        for camera in container:
            for values in addData:
                if camera[eqFild] == values[0]:
                    camera[newfildName] = values[1]
        return container

    def ClearRes(self):
        if os.path.exists("res"):
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'res')
            shutil.rmtree(path)

    def close(self, json_container):
        print("")