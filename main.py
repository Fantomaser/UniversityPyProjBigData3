import os
import zipfile
import requests
import json
import shutil
from tkinter import *



#подчищаем временную папку на случай если программа упала и остались папка с файлами
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

#ответ в кодировке windows-1251
response.encoding = 'windows-1251'

#Временная дирректория чтоб не захламлять
os.mkdir(".\\temp")

#создаем временный zip и записываем туда пришедшее инфо
f = open('.\\temp\\responce.zip', 'wb')
f.write(response.content)
f.close()

#открываем скаченный zip и читаем
z = zipfile.ZipFile('.\\temp\\responce.zip', 'r')
z.extractall(".\\temp")
z.close()

#удаляем больше ненужный zip чтобы остался только 1 файл json
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp\\responce.zip')
os.remove(path)

#В папке будет 1 скачанный файл, читаем его
files = os.listdir(".\\temp")
f = open('.\\temp\\'+files[0], 'r', encoding='windows-1251')

#десериализация в json
cameraInfo = json.loads(f.read())

f.close()

#подчищаем временне файлы после работы программы
if os.path.exists("temp"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp')
    shutil.rmtree(path)

class Window:
    def __init__(self, json_container):
        self.json_container = json_container
        self.window = Tk()
        self.window.title("Добро пожаловать в приложение PythonRu")

        self.work_collaction = [] # пример [mybutton(), mybutton2()]
        self.ptr = 0

        self.btn = Button(self.window, text="back", command=self.clicked_before)
        self.btn.pack( side = LEFT, fill = BOTH )

        self.btn2 = Button(self.window, text="next", command=self.clicked_next)
        self.btn2.pack( side = RIGHT, fill = BOTH )

        self.work_collaction[self.ptr].open(json_container)
        self.window.mainloop()
        
    def clicked_before(self):
        if self.ptr > 0:
            self.work_collaction[self.ptr].close(json_container)
            self.ptr-=1
            self.work_collaction[self.ptr].open(json_container)

    def clicked_next(self):
        if self.ptr < (len(self.work_collaction)-1):
            self.work_collaction[self.ptr].close(json_container)
            self.ptr+=1
            self.work_collaction[self.ptr].open(json_container)


mywindow = Window(cameraInfo)