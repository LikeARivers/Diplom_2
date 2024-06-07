import data


class ChangeTestDataHelper:
    @staticmethod
    def modify_user_body(key, value):
        body = data.DataCreateUser.CREATE_USER_BODY.copy()
        body[key] = value

        return body