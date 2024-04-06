import allure
import datas
from support import Supporting
import requests
import pytest


@allure.feature('Раздел: Логин курьера')
class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_login_courier_successful(self):
        support_method = Supporting()
        login, password, first_name = support_method.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(datas.LOGIN, data=payload)
        assert response.status_code == 200

    @allure.title('Авторизация курьера с некорректным паролем')
    def test_login_with_wrong_password(self):
        support_method = Supporting()
        login, password, first_name = support_method.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": 'wrong'
        }
        response = requests.post(datas.LOGIN, data=payload)
        assert 404 == response.status_code and datas.error_404 in response.text

    @allure.title('Авторизация несуществующего курьера')
    def test_login_non_existent_courier(self):
        payload = {
            "login": 'unknown',
            "password": '12345'
        }
        response = requests.post(datas.LOGIN, data=payload)
        assert 404 == response.status_code and datas.error_404 in response.text

    @allure.title('Авторизация курьера с одним пустым полем')
    @pytest.mark.parametrize("login, password", [
        ("ykarpova", ""),
        ("", "1234567")
    ])
    def test_login_courier_missing_field(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(datas.LOGIN, data=payload)
        assert 400 == response.status_code and datas.error_enter_400 in response.text

    @allure.title('Возврат id при успешной авторизации курьера')
    def test_successful_request_id_return(self):
        support_method = Supporting()
        login, password, first_name = support_method.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(datas.LOGIN, data=payload)
        assert "id" in response.text
