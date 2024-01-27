# Глущенко Юлия, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

# успешное создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                          json=body)

# получение заказа по номеру
def get_order_by_track_number (track_number):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDERS_PATH + str(track_number))

def test_create_order():
    response = post_new_order(data.order_body)
    # проверить, что код ответа равен 201
    assert response.status_code == 201, "Creating order failed with status: " + str(response.status_code)
    track_number = response.json()["track"]
    response = get_order_by_track_number(track_number)
    # проверить, что код ответа равен 200
    assert response.status_code == 200, "Getting order failed with status: " + str(response.status_code)
