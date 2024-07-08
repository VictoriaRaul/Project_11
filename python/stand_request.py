import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_order_by_track(track):
    get_params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=get_params)

# Лузина Виктория, 18-я когорта — Финальный проект. Инженер по тестированию плюс
test_order = data.order_body.copy()
response = post_new_order(test_order)
print("Status code для PUT-запроса создания заказа = ",
      response.status_code)

if response.status_code == 201:
    resp_dict = response.json()
    track = resp_dict["track"]
    print("Track созданного заказа = ", track)

    get_result = get_order_by_track(track)
    print("Status code для GET-запроса информации по заказу с использованием track = ",
          get_result.status_code)
    if get_result.status_code == 200:
        print("GET-запрос информации по заказу с использованием track завершился успешно!")

else:
    print("При создании заказа получен неуспешный status code = ",
          response.status_code)