Проект «Солнечная система»
##########################

:date: 2020-11-02
:summary: Командная работа. Модель движения планет по законам Кеплера. Создание модульной программы.
:status: published

.. default-role:: code
.. contents:: Содержание

Проектирование программы
========================

Командное программирование
--------------------------

Большие проекты создаются только командами программистов, поэтому следует учиться работать над кодом совместно.
Существуют методики `парного программирования`_, хотя чаще встречается разумное разделение труда по программистам за счёт грамотного проектирования_.

.. _парного программирования: https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5

.. _проектирования: https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F

Задание
==========

Легенда
-------

Группа из двух программистов работала над проектом "Солнечная система". Им была поставлена задача -- смоделировать в плоском приближении и визуализировать движение планет Солнечной или подобной ей системы.
Пользовательский интерфейс должен позволять запускать и приостанавливать ход времени.
Столкновение планет друг с другом и с Солнцем моделировать не требуется.
Начальные данные о положении планет, их массах и начальных скоростях считываются из файла.
По запросу пользователя данные о текущем положении, массах и скоростях планет должны сохраняться в файл.

Однако, оба программиста внезапно уволились по невыясненным обстоятельствам.
Вас вызвали, чтобы спасти ситуацию и закончить программу в срок.
К счастью, проект был уже спроектирован и хорошо документирован.

В репозитории проекта лежат файлы модулей, все функции в которых описаны документ-строками.
Разработка остановилась на этапе прототипа, однако он собирается и может быть запущен.

Разбиение на модули
-------------------

Программу предлагается разбить на пять модулей:

* **solar_main.py** — главный модуль
* `solar_objects.py`_ — описание объектов
* `solar_model.py`_ — модуль, отвечающий за моделирование физических объектов
* `solar_vis.py`_ — модуль, отвечающий за интерфейс пользователя
* `solar_input.py`_ — модуль, реализующий чтение и запись в конфигурационные файлы


.. _`solar_objects.py`: {static}/extra/lab10/solar_objects.m.html
.. _`solar_model.py`: {static}/extra/lab10/solar_model.m.html
.. _`solar_vis.py`: {static}/extra/lab10/solar_vis.m.html
.. _`solar_input.py`: {static}/extra/lab10/solar_input.m.html

Распределение ролей
-------------------

Программист А -- старший программист, тимлид.
Зона ответственности: solar_main.py, solar_objects.py, solar_vis.py

Программист В -- второй программист.
Зона ответственности: solar_model.py, solar_input.py

Помните, что важна поэтапность разработки с **работоспособностью при каждом коммите**.



Программист А. План работ
=========================

Постановка задач
----------------

Главная задача тимлида -- организация работ. У него меньше программисткой нагрузки.

В модулях **solar_main.py** и **solar_objects.py** по-видимому всё сделано, исправлений, кажется, не требуется.
Модуль **solar_vis** требует правок по существу.

Этап №0
-------

Для начала тимлид должен **форкнуть репозиторий** к себе на github(т.е. сделать копию в своём аккаунте, кнопка Fork в правом верхнем углу) и **выдать права** на коммит своему подчинённому
программисту (repo->settings->colaborators->add colaborator).

Проект находится в репозитории solar_project_.

.. _solar_project: https://github.com/mipt-cs-on-python3/solar_project

После этого **форкнутый** репозиторий (это важно!) можно склонировать на оба компьютера: тимлида и второго программиста.


Этап №1
-------

Исправить функцию **scale_y** и функцию **create_planet_image** в модуле **solar_vis.py**.

Этап №2
-------

Помогать второму программисту, работая с ним в паре. Вычитывать его код.
Тестировать проект на ошибки.

Программист В. План работ
=========================

Постановка задач
----------------

В модуле solar_model.py не прописана схема вычислений.
В модуле solar_input.py не реализовано считывание и запись в файлы.

Этап №0
-------

Убедиться, что тимлид сделал форк правильно и склонировать **форкнутый им** репозиторий.
Убедиться, что права доступа на коммит есть. Можно сделать тривиальную правку, закоммитить и запушить её на github.

Этап №1
-------

Исправить считывание из файла: функции **parse_star_parameters** и **parse_planet_parameters**.
Эти две функции должны правильным образом заполнить поля уже созданного объекта типа Star и Planet соответственно.

Этап №2
-------

Исправить расчёты физической модели, функцию **calculate_force** и **move_space_object**.

Этап №3
-------

Исправить запись в файл: функцию **write_space_objects_data_to_file**.


Результаты
==========

В результате работы должно получиться следующее

Пример солечной системы
-----------------------

.. image:: {static}/images/lab10/solar_main.gif
   :width: 350 px

Пример двойной звезды
---------------------

.. image:: {static}/images/lab10/double_star.gif
   :width: 350 px

Дополнительное задание
======================

Исправить конфигурационный файл **one_satellite.txt** так, чтобы спутник двигался по эллиптической орбите.

Научиться сохранять статистику вычисленных значений положений и скоростей в файл stats.txt.

Вывести графики:

1. модуля скорости планеты от времени
2. расстояния спутника до звезды от времени
3. модуля скорости от расстояния до звезды

Упражнение 3*. Бранчи в git.
============================

Необходимо создать pull request на гитхабе и вмерджить его. Результат нужно продемонстрировать преподавателю.
Упражнение является логическим продолжением упражнения 1.

1. Перейдем в папку с репозиторием. Создадим новую ветку feature:

.. code-block:: bash

    -> git branch Feature

Теперь у нас есть две ветки (без аргументов branch просто выводит все существующие ветки):

.. code-block:: bash

    -> git branch
    Feature
    * master

2. Давайте переключимся в эту ветку:

.. code-block:: bash

    -> git checkout Feature
    -> git branch
    * Feature
    master

3. История в данной ветке совпадает с историей в master, а вот status пишет, что мы находимся в ветке Feature:

.. code-block:: bash

    -> git log
    commit 8e2642d512b11ae43a97b0b4ac68e802d2626f14
    Author: Egor Khairullin <mikari.san@gmail.com>
    Date:   Wed Nov 9 14:47:40 2016 +0300

        Added something to README

    commit eec733a01ceb6896973998a9327aab735fa40ba4
    Author: Mikari <mikari.san@gmail.com>
    Date:   Wed Nov 9 13:36:38 2016 +0300

        Initial commit
    [15:06:15 Wed Nov 09] mikari@bsnewbt01i:~/tttt/Test(Feature)

    -> git status
    # On branch Feature
    nothing to commit (working directory clean)

4. Давайте добавим новый файл feature и закоммитим его:

.. code-block:: bash

    -> ls
    feature  README.md
    -> git status
    # On branch Feature
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #    feature
    nothing added to commit but untracked files present (use "git add" to track)
    -> git add feature
    -> git commit -m "Added new feature"
    [Feature 446d9f6] Added new feature
     1 file changed, 1 insertion(+)
     create mode 100644 feature
    -> git log
    commit 446d9f6343d0406692fc6012160bed2e19f2fd83
    Author: Egor Khairullin <mikari.san@gmail.com>
    Date:   Wed Nov 9 15:09:26 2016 +0300

        Added new feature

    commit 8e2642d512b11ae43a97b0b4ac68e802d2626f14
    Author: Egor Khairullin <mikari.san@gmail.com>
    Date:   Wed Nov 9 14:47:40 2016 +0300

        Added something to README

    commit eec733a01ceb6896973998a9327aab735fa40ba4
    Author: Mikari <mikari.san@gmail.com>
    Date:   Wed Nov 9 13:36:38 2016 +0300

        Initial commit

Как видим, в git log появился новый коммит. Однако в ветке master этих изменений нет:

.. code-block:: bash

    -> git log master
    commit 8e2642d512b11ae43a97b0b4ac68e802d2626f14
    Author: Egor Khairullin <mikari.san@gmail.com>
    Date:   Wed Nov 9 14:47:40 2016 +0300

        Added something to README

    commit eec733a01ceb6896973998a9327aab735fa40ba4
    Author: Mikari <mikari.san@gmail.com>
    Date:   Wed Nov 9 13:36:38 2016 +0300

        Initial commit

5. Запушим нашу ветку на github.com. Тут нужно обязательно добавить -u origin <branch> к git push для того, чтобы новая ветка создалась и на гитхабе:

.. code-block:: bash

    -> git push -u origin Feature
    Username for 'https://github.com': <username>
    Password for 'https://<username>@github.com': <password>
    To https://github.com/Mikari/Test
     * [new branch]      Feature -> Feature
    Branch Feature set up to track remote branch Feature from origin.

6. Создадим pull request на гитхабе: https://github.com/Mikari/Test/pulls (Кнопка Pull requests в верхнем меню). Нажимаем на New pull request, выбираем base: master, compare: Feature. Там мы можем увидить текущую разницу между нашей новой веткой и мастером. Если все хорошо - нажимаем на Create pull request. Создастся новый pull request, который можно будет вмерджить в наш мастер.

7. Нажмем на Merge pull request. Тут можно увидеть граф коммитов нашего репозитория: https://github.com/Mikari/Test/network (или же Graphs -> Networks). Видно, что наша ветка как бы отпочковалась, а потом вернулась в мастер.

8. Переключимся в нашем локальном репозитории в ветку master и привезем новые изменения:

.. code-block:: bash

    -> git checkout master
    Switched to branch 'master'
    [15:24:04 Wed Nov 09] mikari@bsnewbt01i:~/tttt/Test(master)
    -> git pull
    remote: Counting objects: 1, done.
    remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (1/1), done.
    From https://github.com/Mikari/Test
       8e2642d..d269329  master     -> origin/master
    Updating 8e2642d..d269329
    Fast-forward
     feature |    1 +
     1 file changed, 1 insertion(+)
     create mode 100644 feature

9. Можно увидеть граф нашей истории и в консоли:

.. code-block:: bash

    -> git log --graph --color --all
    *   commit d2693293c55d1325d8adef3a68876d700858b3fd
    |\  Merge: 8e2642d 446d9f6
    | | Author: Mikari <mikari.san@gmail.com>
    | | Date:   Wed Nov 9 15:21:51 2016 +0300
    | |
    | |     Merge pull request #1 from Mikari/Feature
    | |
    | |     Added new feature
    | |
    | * commit 446d9f6343d0406692fc6012160bed2e19f2fd83
    |/  Author: Egor Khairullin <mikari.san@gmail.com>
    |   Date:   Wed Nov 9 15:09:26 2016 +0300
    |
    |       Added new feature
    |
    * commit 8e2642d512b11ae43a97b0b4ac68e802d2626f14
    | Author: Egor Khairullin <mikari.san@gmail.com>
    | Date:   Wed Nov 9 14:47:40 2016 +0300
    |
    |     Added something to README
    |
    * commit eec733a01ceb6896973998a9327aab735fa40ba4
      Author: Mikari <mikari.san@gmail.com>
      Date:   Wed Nov 9 13:36:38 2016 +0300

          Initial commit

10. Вместо создания pull request'а и мерджа через интерфейс можно было бы вмерджить через консоль вот так:

.. code-block:: bash

    -> git checkout master
    -> git merge feature

Продемонстрируйте преподавателю красивый git log в консоли и созданный и закрытый мердж реквест.
