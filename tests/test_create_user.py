import allure
import data
import burgers_api
from conftest import auth_token_clean_created_user
import helper

class TestCreateUser:

    @allure.title("Проверка успешного создания пользователя")
    @allure.description("Создание пользователя с эл. почтой, паролем и именем, проверка статуса и тела ответа")
    def test_success_create_user(self, auth_token_clean_created_user):
        response_create_user = burgers_api.BurgersApi.create_user(data.DataCreateUser.CREATE_USER_BODY)
        assert response_create_user.status_code == 200 and response_create_user.json()["success"] == True

    @allure.title("Проверка ошибки при создании ранее зарегистрированного пользователя")
    @allure.description("Создание ранее зарегистрированного пользователя с эл. почтой, паролем и именем, проверка статуса и тела ответа")
    def test_false_create_registered_user(self, auth_token_clean_created_user):
        response_create_user_one = burgers_api.BurgersApi.create_user(data.DataCreateUser.CREATE_USER_BODY)
        auth_response = burgers_api.BurgersApi.auth_user(data.DataCreateUser.CREATE_USER_BODY)
        response_create_user_two = burgers_api.BurgersApi.create_user(data.DataCreateUser.CREATE_USER_BODY)
        assert response_create_user_two.status_code == 403 and response_create_user_two.json()["success"] == False

    @allure.title("Проверка ошибки при создании пользователя с пустой эл. почтой")
    @allure.description("Создание пользователя с пустой эл. почтой, проверка кода и тела ответа")
    def test_false_create_empty_email_user(self):
        body = helper.ChangeTestDataHelper.modify_user_body("email", "")
        response_create_user = burgers_api.BurgersApi.create_user(body)
        assert response_create_user.status_code == 403 and response_create_user.json()["success"] == False

    @allure.title("Проверка ошибки при создании пользователя с пустым паролем")
    @allure.description("Создание пользователя с пустым паролем, проверка кода и тела ответа")
    def test_false_create_empty_password_user(self):
        body = helper.ChangeTestDataHelper.modify_user_body("password", "")
        response_create_user = burgers_api.BurgersApi.create_user(body)
        assert response_create_user.status_code == 403 and response_create_user.json()["success"] == False

    @allure.title("Проверка ошибки при создании пользователя с пустым именем")
    @allure.description("Создание пользователя с пустым именем, проверка кода и тела ответа")
    def test_false_create_empty_name_user(self):
        body = helper.ChangeTestDataHelper.modify_user_body("name", "")
        response_create_user = burgers_api.BurgersApi.create_user(body)
        assert response_create_user.status_code == 403 and response_create_user.json()["success"] == False
