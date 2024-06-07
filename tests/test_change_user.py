import allure
import data
import burgers_api
from conftest import auth_token_clean_change_user, get_token_create_user, create_user

class TestChangeUser:

    @allure.title("Проверка успешного изменения авторизованного пользователя")
    @allure.description("Изменение эл. почты, пароля и имени пользователя, проверка статуса и тела ответа")
    def test_success_change_user(self, create_user, auth_token_clean_change_user):
        auth_response = burgers_api.BurgersApi.auth_user(data.DataCreateUser.CREATE_USER_BODY)
        user_access_token = auth_response.json().get("accessToken").replace("Bearer ", "")
        response_change_user = burgers_api.BurgersApi.change_user(user_access_token, data.DataCreateUser.CHANGE_USER_BODY)
        assert response_change_user.status_code == 200 and response_change_user.json()["success"] == True

    @allure.title("Проверка ошибки изменения не авторизованного пользователя")
    @allure.description("Изменение эл. почты, пароля и имени пользователя, проверка статуса и тела ответа")
    def test_fall_change_user(self, get_token_create_user, auth_token_clean_change_user):
        response_change_user = burgers_api.BurgersApi.change_user(get_token_create_user, data.DataCreateUser.CHANGE_USER_BODY)
        assert response_change_user.status_code == 401 and response_change_user.json()["success"] == True
    #изменение пользователя без авторизации падает, поскольку сервер позволяет изменить данные пользователя без авторизации, а согласно документации должна быть ошибка