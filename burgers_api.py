import allure
import requests
import urls


class BurgersApi:

    @staticmethod
    @allure.step("Отправка запроса на создание пользователя")
    def create_user(body):
        return requests.post(urls.BASE_URL + urls.CREATE_USER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса на авторизацию пользователя")
    def auth_user(body):
        return requests.post(urls.BASE_URL + urls.AUTH_USER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса на удаление пользователя")
    def delete_user(token):
        headers={'Authorization': f'Bearer {token}'}
        return requests.delete(urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers = headers)

    @staticmethod
    @allure.step("Отправка запроса на изменение пользователя")
    def change_user(token, body):
        headers = {'Authorization': f'Bearer {token}'}
        return requests.patch(urls.BASE_URL + urls.CHANGE_USER_ENDPOINT, headers = headers, json=body)

    @staticmethod
    @allure.step("Отправка запроса на создание заказа")
    def create_order(token, body):
        headers = {'Authorization': f'Bearer {token}'}
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, headers=headers, json=body)

    @staticmethod
    @allure.step("Отправка запроса на получение списка заказов пользователя")
    def get_users_orders(token):
        headers = {'Authorization': f'Bearer {token}'}
        return requests.get(urls.BASE_URL + urls.GET_USERS_ORDERS_ENGPOINT, headers=headers)
