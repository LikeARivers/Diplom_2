import allure
import pytest
import data
import burgers_api

@allure.step("Создание пользователя")
@pytest.fixture(scope='function')
def create_user():
    response_create_user = burgers_api.BurgersApi.create_user(data.DataCreateUser.CREATE_USER_BODY)
    return response_create_user

@allure.step("Получение токена созданного пользователя")
@pytest.fixture(scope='function')
def get_token_create_user(create_user):
    user_access_token = create_user.json().get("accessToken").replace("Bearer ", "")
    return user_access_token

@allure.step("Получение токена и удаление пользователя")
@pytest.fixture(scope='function')
def auth_token_clean_created_user():
    yield
    auth_response = burgers_api.BurgersApi.auth_user(data.DataCreateUser.CREATE_USER_BODY)
    user_access_token = auth_response.json().get("accessToken").replace("Bearer ", "")
    delete_response = burgers_api.BurgersApi.delete_user(user_access_token)

@allure.step("Получение токена и удаление измененного пользователя")
@pytest.fixture(scope='function')
def auth_token_clean_change_user():
    yield
    auth_response = burgers_api.BurgersApi.auth_user(data.DataCreateUser.CHANGE_USER_BODY)
    user_access_token = auth_response.json().get("accessToken").replace("Bearer ", "")
    delete_response = burgers_api.BurgersApi.delete_user(user_access_token)