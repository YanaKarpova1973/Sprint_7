import requests
import datas
import allure

@allure.feature('Раздел: Список заказов')
class TestListOfOrders:
    @allure.title('Тест: Получение списка заказов')
    @allure.description('Получаем список заказов, проверяем статус - код 200, тело ответа содержит "orders"')
    def test_list_of_orders(self):
        response = requests.get(datas.ORDER)
        assert response.status_code == 200 and "orders" in response.json()
