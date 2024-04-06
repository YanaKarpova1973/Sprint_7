import pytest

@pytest.fixture()
def order_data():
    order_data = {
        "firstName": "Яна",
        "lastName": "Карпова",
        "address": "Москва",
        "metroStation": 4,
        "phone": "+79165555555",
        "rentTime": 2,
        "deliveryDate": "2024-04-15",
        "comment": "No comments"
    }
    return order_data
