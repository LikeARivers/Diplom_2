import allure


class DataCreateUser:

    CREATE_USER_BODY = {
        "email": "test_email@yandex.ru",
        "password": "password",
        "name": "Username"
    }

    CHANGE_USER_BODY = {
        "email": "new_email@yandex.ru",
        "password": "newpassword",
        "name": "Newusername"
    }

class DataCreateOrder:
    CREATE_ORDER_BODY = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    EMPTY_ORDER_BODY = {
        "ingredients": []
    }

    FALSE_ORDER_BODY = {
        "ingredients": ["11111111111111", "222222222222222"]
    }