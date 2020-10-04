Игра "Поймай шарик" (часть 1)
#############################

:date: 2020-10-05 09:00
:summary: Обработка событий в Pygame.
:status: draft
:lecture_link: https://youtu.be/ppJfqW7fL80

.. default-role:: code
.. contents:: Содержание


Пользовательский интерфейс
==========================

Приложения с графическим интерфейсом пользователя событийно-ориентированные.
Вы уже должны иметь представление о структурном и желательно объектно-ориентированном программировании.
Событийно-ориентированное ориентировано на события. То есть та или иная часть программного кода начинает выполняться лишь тогда, когда случается то или иное событие.

Событийно-ориентированное программирование базируется на объектно-ориентированном и структурном.
Даже если мы не создаем собственных классов и объектов, то всё равно ими пользуемся. Все виджеты – объекты, порожденные встроенными классами.

События бывают разными. Сработал временной фактор, кто-то кликнул мышкой или нажал Enter,
начал вводить текст, переключил радиокнопки, прокрутил страницу вниз и т. д. Когда случается что-то подобное, то,
если был создан соответствующий обработчик, происходит срабатывание определенной части программы, что приводит к какому-либо результату.


`Pygame` обрабатывает события с помощью **очереди событий**. В неё записываются все происходящие события.
Вспомним код, который использовался в прошлых лабораторных для рисования картины:


.. code-block:: python
    :linenos:

    import pygame
    from pygame.draw import *
    
    pygame.init()
    
    FPS = 30
    screen = pygame.display.set_mode((400, 400))
    
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    
    pygame.quit()  

В цикле используется функция `get()` модуля `event` библиотеки `pygame`  — `pygame.event.get()`. Она забирает список событий из очереди.  Основные события  — это закрытие окна, нажатие и отпускание кнопки мыши, перемещение мыши, нажатие и отпускание клавиши. Узнать, что за событие произошло, позволяет сравнение типа события `event.type` с константой из `pygame`:

.. list-table:: Title
   :widths: 50 50
   :header-rows: 1

   * - Константа
     - Событие
   * - QUIT 
     - закрытие окна
   * - KEYDOWN
     - нажатие клавиши
   * - KEYUP
     - поднятие клавиши
   * - MOUSEMOTION
     - движение мыши
   * - MOUSEBUTTONUP
     - отпускание кнопки мыши
   * - MOUSEBUTTONDOWN
     - нажатие кнопки мыши

Cобытия мыши
============

В `pygame` обрабатываются три события мыши: нажатие кнопки, отпускание кнопки, перемещение мыши. Какая именно кнопка была нажата, записывается в другое свойство события – button. Для левой кнопки это число 1, для средней – 2, для правой – 3, для прокручивания вперед – 4, для прокручивания назад – 5. У событий `MOUSEMOTION` (перемещение мыши) вместо button используется свойство buttons, в которое записывается состояние трех кнопок мыши (кортеж из трех элементов).

Координаты мыши записываются в атрибут `pos`. Таким образом, если вы нажали правую кнопку мыши точно в середине окна размером 200x200, то будет создан объект типа `Event` с полями `event.type = pygame.MOUSEBUTTONDOWN`, `event.button = 3`, `event.pos = (100, 100)`.

У событий `MOUSEMOTION` есть еще один атрибут – `rel`. Он показывает относительное смещение по обоим осям. С помощью него, например, можно отслеживать скорость движения мыши.

Код ниже создаёт круги в местах клика мыши: красные при клике левой кнопкой, синие при клике правой кнопкой.

.. code-block:: python
    :linenos:

    import pygame
    from pygame.draw import *
    pygame.init()
    
    FPS = 30
    screen = pygame.display.set_mode((400, 400))
    
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    circle(screen, RED, event.pos, 50)
                    pygame.display.update()
                elif event.button == 3:
                    circle(screen,  BLUE, event.pos, 50)
                    pygame.display.update()
     
    pygame.quit()

Заготовка игры "Поймай шарик"
=============================

Суть игры проста: в случайном месте появляется на короткое время шарик, и мы должны успеть щелкнуть по нему мышкой.


Вначале создадим появляющиеся шарики:

.. code-block:: python
    :linenos:

    import pygame
    from pygame.draw import *
    from random import randint
    pygame.init()

    FPS = 2
    screen = pygame.display.set_mode((1200, 900))

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

    def new_ball():
        '''рисует новый шарик '''
        x = randint(100, 1100)
        y = randint(100, 900)
        r = randint(10, 100)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        new_ball()
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

Теперь добавим обработку щелчка мыши. Для начала выведем что-нибудь в консоль:

.. code-block:: python
    
    import pygame
    from pygame.draw import *
    from random import randint
    pygame.init()

    FPS = 2
    screen = pygame.display.set_mode((1200, 900))

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

    def new_ball():
        '''рисует новый шарик '''
        x = randint(100, 1100)
        y = randint(100, 900)
        r = randint(10, 100)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        new_ball()
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')

    pygame.quit()

При каждом щелчке в консоли будет появляться надпись «click».

Чтобы определить, попали ли мы в круг, нужно знать его координаты, радиус круга и координаты мыши в момент щелчка. Координаты мыши легко получить через event.pos. Попробуем получить координаты круга:


.. code-block:: python

   def click(event):
       print(x,y,r)  

Такой способ не прошел. Почему? В чем суть появившегося сообщения об ошибке, что оно означает?

Исправим ситуацию:

.. code-block:: python

    def new_ball():
        global x,y,r
        canv.delete(ALL)
        x = rnd(100,700)
        y = rnd(100,500)
        r = rnd(30,50)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)        
        
    def click(event):
        print(x,y,r)   

Использование global – это не самое лучшее решение. Для данной задачи больше подходит использование ООП (объектно-ориентированного подхода), но об этом позже. А пока – будем использовать global.

global означает, что переменные будут считаться глобальными (а не локальными), т.е. их значение сохранится и после завершения работы функции, а не будет уничтожено, как это произойдет со всеми локальными переменными.

Осталось проверить, не лежит ли точка `(event.x, event.y)` дальше, чем r от точки `(x,y)`. Для этого, с помощью теоремы Пифагора мы найдем расстояние между двумя точками и сравним с радиусом круга.

Задания
-------

1. Сделать код читабельным и документированным.
2. Реализовать подсчёт очков.
3. Сделать шарики двигающимися со случайным отражением от стен.
4. Реализовать одновременное присутствие нескольких шариков на экране.
5. * Добавить второй тип мишени со своей формой и своим специфическим харктером движения.
6. * Выдавать за эти мишени другое количество очков.
7. * Сделать таблицу лучших игроков, автоматически сохраняющуюся в файл.



