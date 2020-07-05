class ProjectVova(object):
    def open(self, json container)
import os
import zipfile
import requests
import json
import shutil
from tkinter import
    #Подчищаем временную папку на случай если программа упала и остались папка с файлами
    if os.path.exists("temp"):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp')
        shutil.rmtree(path)
    #Делаем Get запрос для скачивания файла (он в zip)
    response = requests.get("https://op.mos.ru/EHDWSREST/catalog/export/get?id=785973")

    # 200 Reat ответ "Ok"
    if response.status_code != 200:
    print("Server Error")
    else:
    print("Server Ok state")

    #Ответ в кодировке windows-1251
    response.encoding = 'windows-1251'

    #Временная дирректория чтоб не захламлять
    os.mkdir(".\\temp")

    #Создаем временный zip и записываем туда пришедшее инфо
    f = open('.\\temp\\responce.zip', 'wb')
    f.write(response.content)
    f.close()

    #Открываем скаченный zip и читаем
    z = zipfile.ZipFile('.\\temp\\responce.zip', 'r')
    z.extractall(".\\temp")
    z.close()

    #Удаляем больше ненужный zip чтобы остался только 1 файл json
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp\\responce.zip')
    os.remove(path)

    #В папке будет 1 скачанный файл, читаем его
    files = os.listdir(".\\temp")
    f = open('.\\temp\\'+files[0], 'r', encoding='windows-1251')

    #Десериализация в json
    cameraInfo = json.loads(f.read())
    def SummaCamerDmitrov(Dmitrovstkiy, district):
        return sum json.loads


    f.close()
    def close(self, json_container):
        #Функция будет вызываться когда будет закрыт ваш проект
        plt.close(self.fig)