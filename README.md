# Sprint_7
Основная цель проекта: 
Тестирование API учебного сервиса Яндекс Самокат: https://qa-scooter.praktikum-services.ru/

 Проект 7-го спринта имеет следующую структуру:
  
   1. Папка тестов (tests):
       test_courier_creating.py:
            В файле создан класс TestCreateCourier, в который входят методы 
        для тестирования ручек по созданию курьера:
        test_courier_successful_creating   - успешное создание
        test_courier_double_creating       - невозможность создания одинаковых курьеров
        test_courier_creating_with_missing_fields
            - невозможность создания курьера при одном незаполненном поле
        test_courier_creating_without_first_name
            - возможность создания курьера без имени
        
       test_courier_login.py:
            В файле создан класс TestLoginCourier, в который входят методы для 
        тестирования ручек для авторизации курьера
             работы переходов:
        test_login_courier_successful   - Успешная авторизация курьера
        test_login_with_wrong_password  - Авторизация курьера с некорректным паролем
        test_login_non_existent_courier - Авторизация несуществующего курьера
        test_login_courier_missing_field - Авторизация курьера с одним пустым полем
        test_successful_request_id_return - Возврат id при успешной авторизации курьера

       test_list_of_order.py
            В файле создан класс TestListOfOrders, который имеет один метод 
        test_list_of_orders для получения списка заказов

       test_order_making.py
            В файле создан класс TestOrderMaking, который имеет один метод 
        test_make_an_order для cоздания заказа с выбором цвета самоката

Помимо этого в структуру входят файлы:
conftest.py - используемые фикструры в тестах
support.py - файл со вспомогательными методами для регистрации курьера
datas.py - модуль данных с переменными, используемыми для тестов
Папка allure_results