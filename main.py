import os
import zipfile
import requests
import json
import shutil

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
cameraInfo = json.loads(f.read(), encoding='windows-1251')

f.close()

#подчищаем временне файлы после работы программы
if os.path.exists("temp"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp')
    shutil.rmtree(path)

#-------место для вызова сабмодулей для из задания------------


#-------------------------------------------------------------