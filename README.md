# UniversityPyProjBigData3

Для работы рекомендую скачать Visual Studio Code (редактор кода)
https://code.visualstudio.com

Чтобы склонировать репозиторий с кодом:
Скачайте https://git-fork.com
Запустите программу
File->Clone...->
RepositoryUrl = https://github.com/Fantomaser/UniversityPyProjBigData3.git
ParentFolder - Папка в которой будет лежать проет
Name = UniversityPyProjBigData3

Далее жмем правой кнопкой мыши на верхнем коммите (там галочка и написано master и правее origin/master)
Выбираем CreateNewBrunch
Обязательно ставим галочку на checkout after create
Вводим название ветки  - ваша фамилия/название-того-что-вы-делаете
Название слова через "-" низким кейсом

Далее делаем свою работу и находим с лева в fork вкладку Changes
В верхней файлы которые вы поменяли. Выбираем которые надо отправить и жмем stage
С лева с низу "Enter commit subject" вводим изменения кратко
Ниже поле для развернутого пояснения че сделали
Когда ввели жмем Commin
Переходим во вкладку AllCommits и сверху находим то что вводили в описание. Выделяем и жмем на кнопку push


Для работы проекта необходимо выполнить команды:
pip install requests
pip install -U pylint --user (это только для Visual Studio Code)

Просьба оперативно добавлять команды когда необходимы какие-то внешние библиотеки поставить или сконфигурировать питон

Каждый делает свою часть в отдельном файле 
как это сделать см тут - https://metanit.com/python/tutorial/2.10.php

В коде есть часть для вызова своего модуля. Весь код оформляем в виде фугкции пример

def AZAZA( json ):
    #и тут работаем с json выполняя задачу
    #функции называем так чтобы было понятно к какой задаче относится
    #запускаем функции в хронологическом порядке как в задании


Далее задания по пунктам
#######################################################################################
Сергей и вова решите что вы берете есть 2 модуля:
#######################################################################################

-Рассчитать суммарные данные по выбранным столбцам по заданным критериям
    - определить количество камер в Дмитровском районе 
    - определить административный округ в котором максимальное количество камер.
    (Если очень лень можешь просто в консоль вывести, иначе можно визуализировать)
    "Количество камер в Дмитровском районе - много
    В херляндии очень много камер"
//-------------------------------------------------------------------------
-Визуализировать данные с помощью стандартных библиотек по заданным критериям
    построить график, выбрав при этом наиболее подходящий тип графика 
    - количество камер в административных округах с группировкой по каждому району  
    - данные по домам, с максимальным количеством камер. На графике показать 10 домов с адресами, на которых установлено максимальное количество камер

#######################################################################################
Далее идут 4 задания по 2 т.к. они тематически связанны. Никита выбирай что будешь делать
#######################################################################################

Добавить в Dataset данные, полученные в результате промежуточного анализа (вычислений) 
Для всего набора «очищенных» данных добавить столбцы 
    - количества камер в каждом районе 
    - количество камер в каждом округе
Визуализировать данные, полученные в результате промежуточного анализа (вычислений) 
построить сложные графики взаимозависимости 
    - количества камер в каждом районе для 2-х административных округов с самым минимальным количеством камер (по округу) на одном графике 
    - количества камер на домах в пределах одной улицы центрального административного округа. Выбрать все улицы и сгруппировать их по районам
//---------------------------------------------------------------------------------

Получить Dataset (данные) в формате *.txt и/или *.csv из другого источника (графические карты) 
    В качестве источника данных выбрать карты г. Москва. Источник данных найти самостоятельно. 
Визуализировать данные, полученные в результате объединения, для выявления зависимостей между ними 
    Выбрать наиболее подходящий тип графика, который показывал бы есть ли зависимость между величинами из разных полей: 
    - проверить гипотезу: есть ли зависимость между максимальным количеством камер и районами Москвы. Т.е. возможно ли предположение о том, что максимальное количество камер находится в районах Центрального административного округа. Визуализировать данную корреляцию для подтверждения или опровержения данной гипотезы. 
    - показать на карте, используя данные координат (широта, долгота) расположение камер в Центральном административном округе - Дмитровский район. 

