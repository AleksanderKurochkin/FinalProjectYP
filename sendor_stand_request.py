import configuration
import requests
import data

# Создание заказа POST
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)  # Тело запроса

# Получение заказа по номеру трекера GET
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response

# Автотест
def test_order_creation_and_retrieval():
    # Создание заказа
    response = create_order(data.order_body)

    assert response.status_code == 201, f"Ошибка при создании заказа. Код ответа: {response.status_code}"
    track_number = response.json()["track"]
    print("Заказ успешно создан. Номер трека заказа:", track_number)

    # Получение данных о заказе по треку
    order_response = get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка при получении данных о заказе. Код ответа: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные о заказе:")
    print(order_data)