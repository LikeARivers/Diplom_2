import allure
import data
import burgers_api
from conftest import auth_token_clean_created_user, create_user, get_token_create_user

class TestGetUsersOrders:

    @allure.title("Проверка успешного получения списка заказов авторизованного пользователя")
    @allure.description("Получение списка заказов конкретного пользователя, проверка статуса и тела ответа")
    def test_success_get_auth_users_orders(self, create_user, auth_token_clean_created_user):
        auth_response = burgers_api.BurgersApi.auth_user(data.DataCreateUser.CREATE_USER_BODY)
        user_access_token = auth_response.json().get("accessToken").replace("Bearer ", "")
        create_order_response = burgers_api.BurgersApi.create_order(user_access_token, data.DataCreateOrder.CREATE_ORDER_BODY)
        get_users_orders_response = burgers_api.BurgersApi.get_users_orders(user_access_token)
        assert get_users_orders_response.status_code == 200 and get_users_orders_response.json()["success"] == True

    @allure.title("Проверка ошибки получения списка заказов не авторизованного пользователя")
    @allure.description("Получение списка заказов конкретного пользователя, проверка статуса и тела ответа")
    def test_success_get_users_orders(self, create_user, get_token_create_user, auth_token_clean_created_user):
        create_order_response = burgers_api.BurgersApi.create_order(get_token_create_user,
                                                                    data.DataCreateOrder.CREATE_ORDER_BODY)
        get_users_orders_response = burgers_api.BurgersApi.get_users_orders(get_token_create_user)
        assert get_users_orders_response.status_code == 401 and get_users_orders_response.json()["success"] == False
