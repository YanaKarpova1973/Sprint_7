from support import Supporting
import requests
import datas
import pytest
import allure

@allure.feature('Раздел: Создание курьера')
class TestCreateCourier:
    @allure.title('Тест: Проверка успешного создания курьера: ожидаемые код и текст ответа об успешном создании')
    def test_courier_successful_creating(self):
        support_method = Supporting()
        payload = support_method.courier_datas_creation(7)
        response = requests.post(datas.COURIER_CREATION, data=payload)
        assert response.status_code == 201 and datas.successful_message in response.text

    @allure.title('Тест: нельзя создать двух одинаковых курьеров')
    @allure.description('В данных передаем логин который был ранее зарегистрирован, проверяем код 409 и тело ответа')
    def test_courier_double_creating(self):
        response = requests.post(datas.COURIER_CREATION, datas.double_courier)
        assert response.status_code == 409 and datas.error_409 in response.text

    @allure.title('Тест: Отсутствие одного из обязательных полей, запрос возвращает ошибку')
    @allure.description('В данных передаем данные сначала без логина, потом без пароля, проверяем код 400 и тело ответа')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_creating_with_missing_fields(self, missing_field):
        support_method = Supporting()
        payload = support_method.courier_datas_creation(7)
        del payload[missing_field]
        response = requests.post(datas.COURIER_CREATION, data=payload)
        assert response.status_code == 400 and datas.error_account_400 in response.text

    @allure.title('Тест: Создание курьера без имени')
    def test_courier_creating_without_first_name(self):
        support_method = Supporting()
        payload = support_method.courier_datas_creation(7)
        del payload["firstName"]
        response = requests.post(datas.COURIER_CREATION, data=payload)
        assert response.status_code == 201 and datas.successful_message in response.text
