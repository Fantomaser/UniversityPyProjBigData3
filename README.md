# UniversityPyProjBigData3

## Для работы рекомендую скачать Visual Studio Code (редактор кода)
https://code.visualstudio.com

## Надо настроить Git
- Регаемся тут https://github.com
- Качаем и настраиваем вот это https://git-scm.com/downloads

## Чтобы склонировать репозиторий с кодом:
- Скачайте https://git-fork.com
- Запустите программу
- File->Clone...->
- RepositoryUrl = https://github.com/Fantomaser/UniversityPyProjBigData3.git
- ParentFolder - Папка в которой будет лежать проет
- Name = UniversityPyProjBigData3

## Создаем новую ветку
Далее жмем правой кнопкой мыши на верхнем коммите (там галочка и написано master и правее origin/master)
Выбираем CreateNewBrunch
Обязательно ставим галочку на checkout after create
Вводим название ветки  - ваша фамилия/название-того-что-вы-делаете
Название слова через "-" низким кейсом

## Заливка данных
- Далее делаем свою работу и находим с лева в fork вкладку Changes
- В верхней части файлы которые вы поменяли. Выбираем которые надо отправить и жмем stage
- С лева с низу "Enter commit subject" вводим изменения кратко
- Ниже поле для развернутого пояснения че сделали
- Когда ввели жмем Commin
- Переходим во вкладку AllCommits и сверху находим то что вводили в описание. Выделяем и жмем на кнопку push


## Для работы проекта необходимо выполнить команды:
* pip install requests
* pip install folium // для карт
* pip install python-tk
* pip install -U pylint --user (это только для Visual Studio Code)
* python -mpip install -U matplotlib (будем использовать matplotlib) объяснение библиотеки можно найти тут https://python-scripts.com/matplotlib
- (Спойлер) не обязательно читать начало и историю, можно начать с примеров и делать по подобию 

# Просьба добавлять команды когда необходимы какие-то внешние библиотеки поставить или сконфигурировать питон

### Информация по json
https://python-scripts.com/json

#### Каждый делает свою часть в отдельном файле 
- Как это сделать см тут - https://metanit.com/python/tutorial/2.10.php

#### Весь код оформляем в виде класса с функциями close и open с обязательным параметром json_container

- Как это сделать см тут - https://metanit.com/python/tutorial/7.1.php

### Пример класса:

```
class ProjectVova:
    def open(self, json_container):
        #Функция будет вызываться когда будет открыт ваш проект
        #и тут работаем с json выполняя задачу
        #функции называем так чтобы было понятно к какой задаче относится
        #запускаем функции в хронологическом порядке как в задании

        rng = np.arange(100)
        rnd = np.random.randint(0, 10, size=(3, rng.size))
        yrs = 1950 + rng
            
        self.fig, ax = plt.subplots(figsize=(5, 3))
        ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
        ax.set_title('Combined debt growth over time')
        ax.legend(loc='upper left')
        ax.set_ylabel('Total debt')
        ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
        self.fig.tight_layout()
        plt.show()

    def close(self, json_container):
        #Функция будет вызываться когда будет закрыт ваш проект
        plt.close(self.fig)

```

- json_container - это списки в списках сделанные на основе вот этого файла https://op.mos.ru/EHDWSREST/catalog/export/get?id=785973

- Так же необходимо в 62 строке файлa main.py по примеру добавить ваш класс

- Воизбежание дальнейших вопросов напоминаю 
надо подключить свой модуль в файле main.py чтобы испльзовать свой код

## Далее задания по пунктам

### Вова

- [x] Рассчитать суммарные данные по выбранным столбцам по заданным критериям
* определить количество камер в Дмитровском районе 
* определить административный округ в котором максимальное количество камер.
    (Если очень лень можешь просто в консоль вывести, иначе можно визуализировать)
    "Количество камер в Дмитровском районе - много
    В херляндии очень много камер"
____
### Сергей
- [ ] Визуализировать данные с помощью стандартных библиотек по заданным критериям, построить график, выбрав при этом наиболее подходящий тип графика 
* количество камер в административных округах с группировкой по каждому району  
* данные по домам, с максимальным количеством камер. На графике показать 10 домов с адресами, на которых установлено максимальное количество камер
___
### Никита

- [x] Добавить в Dataset данные, полученные в результате промежуточного анализа (вычислений). Для всего набора «очищенных» данных добавить столбцы 
* количества камер в каждом районе
* количество камер в каждом округе
- [ ] Визуализировать данные, полученные в результате промежуточного анализа (вычислений) построить сложные графики взаимозависимости 
* количества камер в каждом районе для 2-х административных округов с самым минимальным количеством камер (по округу) на одном графике 
* количества камер на домах в пределах одной улицы центрального административного округа. Выбрать все улицы и сгруппировать их по районам
### Женя
____

- [x] Получить Dataset (данные) в формате *.txt и/или *.csv из другого источника (графические карты) 
* В качестве источника данных выбрать карты г. Москва. Источник данных найти самостоятельно. 
- [x] Визуализировать данные, полученные в результате объединения, для выявления зависимостей между ними 
* Выбрать наиболее подходящий тип графика, который показывал бы есть ли зависимость между величинами из разных полей: 
* проверить гипотезу: есть ли зависимость между максимальным количеством камер и районами Москвы. Т.е. возможно ли предположение о том, что максимальное количество камер находится в районах Центрального административного округа. Визуализировать данную корреляцию для подтверждения или опровержения данной гипотезы. 
* показать на карте, используя данные координат (широта, долгота) расположение камер в Центральном административном округе - Дмитровский район.  

