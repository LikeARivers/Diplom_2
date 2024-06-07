import allure
import data
import burgers_api
from conftest import auth_token_clean_created_user
import helper

class TestAuthUser:

    @allure.title("Проверка успешного логина пользователя")
    @allure.description("Логин пользователя с эл. почтой, паролем и именем, проверка статуса и тела ответа")
    def test_success_auth_user(self, auth_token_clean_created_user):
        response_create_user = burgers_api.BurgersApi.create_user(data.DataCreateUser.CREATE_USER_BODY)
        auth_response = burgers_api.BurgersApi.auth_user(data.DataCreateUser.CREATE_USER_BODY)
        assert auth_response.status_code == 200 and auth_response.json()["success"] == True

    @allure.title("Проверка ошибки при логине пользователя с неверной эл. почтой")
    @allure.description("Логин пользователя с неверной эл. почтой, проверка кода и тела ответа")
    def test_false_auth_incorrect_email_user(self, auth_token_clean_created_user):
        body = helper.ChangeTestDataHelper.modify_user_body("email", "abcd@yandex.ru")
        response_create_user = burgers_api.BurgersApi.create_user(data.DataCreateUser.CREATE_USER_BODY)
        auth_response = burgers_api.BurgersApi.auth_user(body)
        assert auth_response.status_code == 401 and auth_response.json()["success"] == False

    @allure.title("Проверка ошибки при логине пользователя с неверным паролем")
    @allure.description("Логин пользователя с неверным паролем, проверка кода и тела ответа")
    def test_false_auth_incorrect_password_user(self, auth_token_clean_created_user):
        body = helper.ChangeTestDataHelper.modify_user_body("password", "abcd123")
        response_create_user = burgers_api.BurgersApi.create_user(data.DataCreateUser.CREATE_USER_BODY)
        auth_response = burgers_api.BurgersApi.auth_user(body)
        assert auth_response.status_code == 401 and auth_response.json()["success"] == False
