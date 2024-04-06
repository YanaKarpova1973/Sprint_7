import requests
import datas
import pytest
import allure

@allure.feature('Раздел: Создание заказа')
class TestOrderMaking:
    
    @allure.title('Создание заказа с выбором цвета самоката')
    @pytest.mark.parametrize("colour", ["BLACK", "GREY", "", "BLACK, GREY"])
    def test_make_an_order(self, colour, order_data):
        payload = order_data
        payload["color"] = [colour]
        response = requests.post(datas.ORDER, json=payload)
        assert response.status_code == 201 and "track" in response.json()
