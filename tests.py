import sender_stand_request
import data

#Азизов Мехроб 23 когорта - Финальный проект

def test_get_order_info_track():
    track = sender_stand_request.new_order(data.order_body).json()['track']
    response = sender_stand_request.get_order_info_by_track(track)
    assert response.status_code == 200