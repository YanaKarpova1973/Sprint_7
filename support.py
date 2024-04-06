import requests
import random
import string


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
class Supporting:
# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def courier_datas_creation(self, length):
        login = self.generate_random_string(length)
        password = self.generate_random_string(length)
        first_name = self.generate_random_string(length)
        payload = {"login": login, "password": password, "firstName": first_name}
        return payload

    def register_new_courier_and_return_login_password(self):
        # создаём список, чтобы метод мог его вернуть
        login_pass = []
        payload = self.courier_datas_creation(10)

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(payload['login'])
            login_pass.append(payload['password'])
            login_pass.append(payload['firstName'])

        # возвращаем список
        return login_pass
