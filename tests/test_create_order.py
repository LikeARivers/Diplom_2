import allure
import pytest
import data
import burgers_api
from conftest import create_user, auth_token_clean_created_user, get_token_create_user

class TestCreateOrder:

    @allure.title("Проверка создания заказа с авторизацией")
    @allure.description("Создание заказа авторизованным пользователем, проверка кода и тела ответа")
    @pytest.mark.parametrize("order_body, expected_status_code, expected_json_response, description", [
        (data.DataCreateOrder.CREATE_ORDER_BODY, 200, True, "с ингредиентами"),
        (data.DataCreateOrder.EMPTY_ORDER_BODY, 400, False, "с пустым телом"),
    ])
    def test_create_order_auth_user(self, create_user, order_body, expected_status_code, expected_json_response, description, auth_token_clean_created_user):
        auth_response = burgers_api.BurgersApi.auth_user(data.DataCreateUser.CREATE_USER_BODY)
        user_access_token = auth_response.json().get("accessToken").replace("Bearer ", "")
        create_order_response = burgers_api.BurgersApi.create_order(user_access_token, order_body)
        assert create_order_response.status_code == expected_status_code and create_order_response.json()["success"] == expected_json_response

    @allure.title("Проверка создания заказа без авторизации")
    @allure.description("Создание заказа не авторизованным пользователем, проверка кода и тела ответа")
    @pytest.mark.parametrize("order_body, expected_status_code, expected_json_response, description", [
        (data.DataCreateOrder.CREATE_ORDER_BODY, 200, True, "с ингредиентами"),
        (data.DataCreateOrder.EMPTY_ORDER_BODY, 400, False, "с пустым телом"),
    ])
    def test_create_order_no_auth_user(self, get_token_create_user, order_body, expected_status_code, expected_json_response, description, auth_token_clean_created_user):
        create_order_response = burgers_api.BurgersApi.create_order(get_token_create_user, order_body)
        assert create_order_response.status_code == expected_status_code and create_order_response.json()["success"] == expected_json_response

    @allure.title("Проверка создания заказа с авторизацией, с невалидным хэшем")
    @allure.description("Создание заказа авторизованным пользователем, с невалидным хэшем, проверка кода и тела ответа")
    def test_create_invalid_order_auth_user(self, create_user, auth_token_clean_created_user):
        auth_response = burgers_api.BurgersApi.auth_user(data.DataCreateUser.CREATE_USER_BODY)
        user_access_token = auth_response.json().get("accessToken").replace("Bearer ", "")
        create_order_response = burgers_api.BurgersApi.create_order(user_access_token, data.DataCreateOrder.FALSE_ORDER_BODY)
        assert create_order_response.status_code == 500 and "Internal Server Error" in create_order_response.text

    @allure.title("Проверка создания заказа без авторизации, с невалидным хэшем")
    @allure.description("Создание заказа не авторизованным пользователем, с невалидным хэшем, проверка кода и тела ответа")
    def test_create_invalid_order_no_auth_user(self, get_token_create_user, auth_token_clean_created_user):
        auth_response = burgers_api.BurgersApi.auth_user(data.DataCreateUser.CREATE_USER_BODY)
        user_access_token = auth_response.json().get("accessToken").replace("Bearer ", "")
        create_order_response = burgers_api.BurgersApi.create_order(user_access_token, data.DataCreateOrder.FALSE_ORDER_BODY)
        assert create_order_response.status_code == 500 and "Internal Server Error" in create_order_response.text