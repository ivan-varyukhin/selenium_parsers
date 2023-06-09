## **Парсеры с использованием библиотеки Selenium**

***fill_input.py***

    Необходимо на сайте http://parsinger.ru/selenium/1/1.html с помощью Selenium
    заполнить все существующие поля и нажмите на кнопку, при этом уложившись в 5 секунд
    Получить результат, который появится рядом с кнопкой.

***find_link.py***

    Необходимо на сайте http://parsinger.ru/selenium/2/2.html с помощью Selenium
    при помощи метода By.PARTIAL_LINK_TEXT или By.LINK_TEXT кликнуть по ссылке с текстом 16243162441624;
    Получить результат в теге <p id="result"></p>

***sum_300p.py***

    Необходимо на сайте http://parsinger.ru/selenium/3/3.html с помощью Selenium
    извлечь данные из каждого тега <p> и сложить все значения (всего 300 шт).

***sum_300p_2.py***

    Необходимо на сайте http://parsinger.ru/selenium/3/3.html с помощью Selenium
    извлечь данные из каждого  второго тега <p> и сложить все значения (всего 100 шт).

***make_all_checked.py***

    Необходимо на сайте http://parsinger.ru/selenium/4/4.html с помощью Selenium
    установить все чек боксы в положение checked при помощи метода click().
    Когда все чек боксы станут активны, нажать на кнопку.
    Получить результат появится в <p id="result">Result</p>

***make_some_checked.py***

    Необходимо на сайте http://parsinger.ru/selenium/5/5.html с помощью Selenium
    установить чек боксы в положение checked при помощи метода click().
    Должны быть установлены те чек боксы, значение value="" которых, есть в списке numbers.
    Когда все необходимые чек боксы станут checked, кнопка станет активной, 
    нажать на неё и получить результат в <p id="result">Result</p>.

***sum_drop-down_list.py***

    Необходимо на сайте http://parsinger.ru/selenium/7/7.html с помощью Selenium
    получить значения всех элементов выпадающего списка и суммировать их.
    Затем вставить получившийся результат в поле на сайте, нажать кнопку и получить результат.

***calc_result_and_find_element.py***

    Необходимо на сайте http://parsinger.ru/selenium/6/6.html с помощью Selenium
    найти значение выражения на странице, затем выбрать в  выпадающем списке элемент с числом, 
    которое у вас получилось после нахождения значения уравнения, нажать кнопку и получить результат.

***many_refresh_for_number.py***

    Необходимо на сайте https://parsinger.ru/methods/1/index.html с помощью Selenium
    обновлять страницу пока в id="result" появится число (возможно много раз, т.к. число появляется не часто).

***sum_secret_cookies.py***

    Необходимо на сайте https://parsinger.ru/methods/3/index.html с помощью Selenium
    получить все значения "секретных" cookie и суммировать их.


***sum_even_secret_cookies.py***

    Необходимо на сайте https://parsinger.ru/methods/3/index.html с помощью Selenium
    получить все значения cookie с чётным числом после "_" и суммировать их.


***find_long-life_cookie.py***

    Необходимо на сайте https://parsinger.ru/methods/5/index.html с помощью Selenium
    посетить все 42 ссылки,найти среди них страницу с самым длинным сроком жизни cookie,
    и получить с этой страницы число.

***scroll_click_and_sum.py***

    Необходимо на сайте http://parsinger.ru/scroll/4/index.html с помощью Selenium
    Нажать поочередно 50 кнопок, которые визуально перекрыты блоками.
    После нажатия на кнопку в id="result" появляется уникальное для каждой кнопки число.
    Собрать уникальные числа и суммировать их.

***scroll_click_and_sum_2.py***

    Необходимо на сайте http://parsinger.ru/scroll/2/index.html с помощью Selenium
    включить 100 чекбоксов (25 из них вернут число) и суммировать все появившиеся числа.

***scroll_click_and_sum_500.py***

    Необходимо на сайте http://parsinger.ru/scroll/3/ с помощью Selenium
    получить числовые значения  id="число" с каждого тега <input>, который при нажатии вернул число,
    и суммировать эти значения (на целевом сайте 500 тегов).


***scroll_100elems_and_sum.py***

    Необходимо на сайте http://parsinger.ru/infiniti_scroll_1/ с помощью Selenium
    получить все значения в элементах и суммировать их.

    На сайте есть список из 100 элементов, которые генерируются при скроллинге.
    В списке есть интерактивные элементы, по которым можно осуществить скроллинг вниз
    (можно использовать Keys.DOWN или .move_to_element()).
    Последний элемент в списке имеет class="last-of-list".

***scroll_100elems_and_sum_2.py***

    Необходимо на сайте http://parsinger.ru/infiniti_scroll_2/ с помощью Selenium
    прокрутить список из 100 элементов, которые генерируются при скроллинге в самый низ,
    получить все значения в элементах и суммировать их.
    Для скроллинга окна использовать .scroll_by_amount(delta_x, delta_y) 

***scroll_5x100elems_and_sum.py***

    Необходимо на сайте http://parsinger.ru/infiniti_scroll_3/ с помощью Selenium 
    прокрутить все 5 окошек с подгружаемыми элементами (в каждом по 100 элементов) в самый низ,
    получить все значение в каждом из окошек и суммировать их.


***click_100buttons_and_find_code.py***

    Необходимо на сайте http://parsinger.ru/blank/modal/2/index.html с помощью Selenium
    найти секретный код, который появляется при нажатии на одну из 100 кнопок в  теге <p id="result">Code</p>

***click_100buttons_and_check_pin_code.py***

    Необходимо на сайте http://parsinger.ru/blank/modal/3/index.html с помощью Selenium
    найти правильный пин-код и получить секретный код.

    На сайте есть 100 buttons.
    При нажатии на любую кнопку появляется confirm с пин-кодом.
    Текстовое поле под кнопками проверяет правильность пин-кода.

***find_correct_pin_code.py***

    Необходимо на сайте http://parsinger.ru/blank/modal/4/index.html с помощью Selenium
    найти правильный пин-код и получить секретный код.

    На сайте есть список пин-кодов и только один правильный;
    Для проверки пин-кода используйте кнопку "Проверить"

***open_window_555x555.py***

    Открыть сайт http://parsinger.ru/window_size/1/ с помощью Selenium.
    Необходимо открыть окно таким размером, чтобы рабочая область страницы составляла 555px на 555px
    Учитывайте размеры границ браузера.
    Результат появится в id="result".

***open_window_with_correct_size.py***

    Открыть сайт http://parsinger.ru/window_size/2/index.html с помощью Selenium.
    Есть 2 списка с размерами  size_x и size_y, при единственном правильном сочетании размеров
	из этих списков, появится число. Результат появится в id="result".
    Учитывайте размер рамок браузера.

    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

***open_window_and_get_correct_size.py***

    Открыть сайт http://parsinger.ru/window_size/2/index.html с помощью Selenium.
    Есть 2 списка с размера окон size_x и size_y.
    Необходимо определить размер окна, при котором,  в id="result" появляется число.
    Учитывайте размер рамок браузера.

    Результат должен быть в виде словаря {'width': size_x, 'height': size_y}, 
    где размеры указаны без учёта размеров рамок браузера, т.е. необходимо указать размер
	рабочей области браузера.

    window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

***сlick_buttons_and_sum_titles.py***

    Открыть сайт http://parsinger.ru/blank/3/index.html с помощью Selenium.
    На сайте есть 10 buttons, каждый button откроет сайт в новой вкладке, каждая вкладка имеет в title
	уникальное число.
    Необходимо собрать числа с каждой вкладки и суммировать их.

***open_tabs_click_and_sum.py***

    Есть список сайтов (6 шт), на каждом сайте есть chekbox, при нажатии на этот chekbox появляется код.
    Необходимо открыть с помощью Selenium все сайты во вкладках (.window_handles), пройти в цикле по каждой
	вкладке, нажать на chekbox и получить код.
    Из каждого числа, необходимо извлечь корень, функцией sqrt(), суммировать получившиеся корни 
	и получить результат.
   
    Верный ответ содержит  9 знаков после запятой, т.е имеет вид 000000.000000000, 
	для округления используйте функцию round()
 
    sites = ['http://parsinger.ru/blank/1/1.html', 
             'http://parsinger.ru/blank/1/2.html',
			 'http://parsinger.ru/blank/1/3.html',
			 'http://parsinger.ru/blank/1/4.html',
			 'http://parsinger.ru/blank/1/5.html',
			 'http://parsinger.ru/blank/1/6.html',]

***catch_title_and_get_result.py***

    Открыть сайт http://parsinger.ru/expectations/3/index.html с помощью Selenium.
    На сайте есть кнопка, которая становится активной после загрузки страницы со случайной задержкой
	(от 1 до 3 сек).
    После нажатия на кнопку, в title начнут появляться коды, со случайным временем (от 0.1 до 0.6 сек).
    Необходимо успеть получить код из id="result", когда  title будет равен "345FDG3245SFD";

***catch_title_by_part.py***

    Открыть сайт http://parsinger.ru/expectations/4/index.html с помощью Selenium.
    На сайте есть кнопка, которая становится активной после загрузки страницы со случайной задержкой
	(от 1 до 3 сек).
    После нажатия на кнопку, в title начнут появляться коды, со случайным временем (от 0.1 до 0.6 сек).
    Необходимо получить title целиком, если title содержит "JK8HQ"

***catch_class_and_get_result.py***

    Открыть сайт http://parsinger.ru/expectations/5/index.html с помощью Selenium.
    На сайте есть кнопка, которая становится активной после загрузки страницы со случайной задержкой
	(от 1 до 3 сек).
    После нажатия на кнопку, на странице начнётся создание элементов class со случайными значениями.
    Необходимо получить содержимое элемента с классом "BMH21YY", когда он появится на странице.

***catch_class_and_get_result_2.py***

    Открыть сайт http://parsinger.ru/expectations/6/index.html с помощью Selenium.
    На сайте есть кнопка, которая становится активной после загрузки страницы со случайной задержкой
	(от 1 до 3 сек).
    После нажатия на кнопку, на странице начнётся создание элементов class со случайными значениями.
    Необходимо получить  содержимое элемента с классом "Y1DM2GR" , когда он появится на странице.

***drag_and_drop_block.py***

    Необходимо на сайте https://parsinger.ru/draganddrop/1/index.html c помощью Selenium
    перетащить красный блок из первого поля во второе.
    После перемещения блока, появится токен.

***drag_and_drop_4block.py***

    Необходимо на сайте https://parsinger.ru/draganddrop/2/index.html c помощью Selenium
    перетащить красный квадрат поочерёдно в каждый блок.
    После перемещения красного квадрата по всем блокам, появится токен.

***drag_and_drop_square.py***

    Необходимо на сайте https://parsinger.ru/draganddrop/3/index.html c помощью Selenium
    Перетащить синий квадрат по оси X поочерёдно сквозь все красные точки.
    После перемещения синего квадрата по всем точкам, появится токен.
