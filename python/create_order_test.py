import data
import sender_stand_request

# Лузина Виктория, 18-я когорта — Финальный проект. Инженер по тестированию плюс
def test_create_order_and_get_order_info():
    test_order = data.order_body.copy()
    response = sender_stand_request.post_new_order(test_order)

    assert response.status_code == 201

    resp_dict = response.json()
    track = resp_dict["track"]
    print("Track созданного заказа = ", track)

    get_result = sender_stand_request.get_order_by_track(track)

    assert get_result.status_code == 200
    print("GET-запрос информации по заказу с использованием track завершился успешно!")