import configuration
import requests
import data

def post_new_user(user_data):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=user_data,  # тут тело
                         headers=data.headers)  # а здесь заголовки

# response = post_new_user(user_data)

# print(response.status_code)
# print(response.json())
