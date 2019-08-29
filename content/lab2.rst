Игра «Поймай шарик»
#################################

:date: 2018-10-19 09:00
:summary: Техника безопасности и эргономика.
:status: draft


.. default-role:: code


Введение в tkinter
==================

tkinter (от англ. tk interface) - это графическая библиотека, позволяющая создавать программы с оконным интерфейсом.

Эта библиотека является интерфейсом к популярному языку программирования и инструменту создания графических приложений tcl/tk. tkinter, как и tcl/tk, является кроссплатформенной библиотекой и может быть использована в большинстве распространённых операционных систем (Windows, Linux, Mac OS X и др.).

tkinter это стандартная библиотека языка python. Подробнее советую прочитать `здесь <https://younglinux.info/tkinter.php>`_, `здесь <https://ru.wikiversity.org/wiki/Курс_по_библиотеке_Tkinter_языка_Python>`__ или `здесь <http://effbot.org/tkinterbook/>`__.

Основные классы
===============
``Tk`` - главная форма.

``Canvas`` - полотно для рисования.

``Button`` - кнопка.

``Label`` - метка.

``Entry`` - однострочное текстовое поле.


Создадим простую программу
=====================================


.. code-block:: python

    from tkinter import *

    root = Tk()
    root.geometry('800x600')        # размер окна 800x600
    canv = Canvas(root, bg='white') # создать в окне root, фон - белый
    canv.pack(fill=BOTH, expand=1)  # размер - максимально возможный в обе стороны

    # рисуем простые фигуры
    canv.create_rectangle(50, 50, 100, 100, fill='red')
    canv.create_line(0, 0, 150, 300, width=5)
    canv.create_oval(200, 200, 500, 500)
    canv.create_text(350, 350, text=u'МФТИ')

    mainloop()


Как можно заметить круг задаётся координатоми описаного вокруг него квадрата. Это не очень удобно.

Задание:
--------
Вам даны координаты центра круга, его цвет и радиус. Нарисуйте этот круг.

.. code-block:: python

    from tkinter import *
    root = Tk()
    root.geometry('800x600')
    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)

    x = y = 300
    r = 130
    color = 'green'

    # ваш код здесь

    canv.create_oval(...)

    # конец вашего кода

    mainloop()

Обработка событий
=================

Добавим обработку нажатий кнопок мыши. Для начала просто будем писать что-то в консоль.

.. code-block:: python

    from tkinter import *
    root = Tk()
    root.geometry('800x600')
    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)

    def left_click(event):
        print('left click')

    def right_click(event):
        print('right click')

    canv.bind('<Button-1>', left_click)
    canv.bind('<Button-3>', right_click)

    mainloop()

Как обрабатывать события
------------------------

+---------------+------------------------------------------------------------------------+
| "<Button-№>"  |  Нажатие кнопки мыши 1, 2 или 3.                                       |
+---------------+------------------------------------------------------------------------+
| "<k>"         |  Нажатие на клавиатуре кнопки k.                                       |
+---------------+------------------------------------------------------------------------+
| "<B№-Motion>" |  Одновременное движения курсора мыши и нажатия на одну из кнопок мыши. |
+---------------+------------------------------------------------------------------------+

Задание:
--------

Измените код так, чтобы на месте левого клика мышкой рисовался круг случайного цвета (у объекта ``event`` есть поля ``x`` и ``y``).
А когда кликнем правой кнопкой, холст очищался (поможет функция ``canv.delete(ALL)``).

Таймеры
=======

С помощью этих методов вы можете отложить выполнение какого-нибудь кода на определённое время.

``after`` - принимает два аргумента: время в миллисекундах и функцию, которую надо выполнить через указанное время. Возвращает идентификатор, который может быть использован в ``after_cancel``.

``after_idle`` - принимает один аргумент - функцию. Эта функция будет выполнена после завершения всех отложенных операций (после того, как будут обработаны все события). Возвращает идентификатор, который может быть использован в ``after_cancel``.

``after_cancel`` - принимает один аргумент: идентификатор задачи, полученный предыдущими функциями, и отменяет это задание.

Пример, часы:
-------------

.. code-block:: python

    from tkinter import *
    import time


    def tick():
        root.after(200, tick)
        canv.delete(ALL)
        canv.create_text(400, 300, text=time.strftime('%H:%M:%S'), font='Arial 25')


    root = Tk()
    root.geometry('800x600')

    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)

    root.after_idle(tick)
    root.mainloop()

Задание:
--------

#. Напишите программу, которая будет рисовать шарик случайного цвета и размера в случайном месте на экране каждую секунду.

#. Теперь добавим возможность кликать мышкой и выведем на экран счётчик очков (``create_text``). Если координаты курсора оказались внутри шарика (отстоят от центра меньше чем на радиус) то увеличим счётчик очков на 1.




Шуточный пример
---------------

.. code-block:: python

    import tkinter as tk

    def my_button_handler(event):
        var.set(1)

    root = tk.Tk()

    var = tk.IntVar(root, 1)
    label = tk.Label(root, text="Do you want to marry me?", font="Arial 30")
    rbutton1 = tk.Radiobutton(root, text='Yes', variable=var, value=1, font="Arial 30")
    rbutton2 = tk.Radiobutton(root, text='No', variable=var, value=2, font="Arial 30")
    button1 = tk.Button(root, text="OK", font="Arial 30")

    for widget in label, rbutton1, rbutton2, button1:
        widget.pack()

    button1.bind("<Motion>", my_button_handler)

    root.mainloop()

Делаем игру интересней
----------------------

.. code-block:: python

    from tkinter import *

    root = Tk()
    root.geometry("300x300")
    canvas = Canvas(root)
    x, y = 100, 100
    dx, dy = 2, 3
    oval = canvas.create_oval(x, y, x+40, y+40)
    canvas.pack(fill=BOTH, expand=1)

    def tick_handler():
        global x, y, dx, dy
        print("Тик!")
        # Отражение от края холста
        if x < 0:
            dx = -dx; x = 0
        elif x > 300-40:
            dx = -dx
            x = 300-40
        if y < 0:
            dy = -dy
            y = 0
        elif y > 300-40:
            dy = -dy
            y = 300-40
        x = x + dx; y = y + dy
        canvas.move(oval, dx, dy)


    def time_handler():
        global freeze
        speed = speed_scale.get()
        if speed == 0:
            print("Заморозка!")
            freeze = True
            return
        tick_handler()
        sleep_dt = 1100 - 100*speed
        root.after(sleep_dt, time_handler)

    def unfreezer(event):
        global freeze
        if freeze == True:
            speed = speed_scale.get()
            if speed != 0:
                freeze = False
                root.after(0, time_handler)

    speed_scale = Scale(root, orient=HORIZONTAL, length=300,
                   from_=0, to=10, tickinterval=1, resolution=1)
    speed_scale.pack()

    # Скорость = 1
    speed_scale.set(1);
    freeze = False

    root.after(10, time_handler)
    speed_scale.bind("<Motion>", unfreezer)
    root.mainloop()


Задание:
--------

#. Сделайте код сверху красивым, добавьте побольше летающих шариков, и их взаимодействие