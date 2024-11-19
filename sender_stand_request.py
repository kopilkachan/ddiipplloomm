import configuration
import requests
import data

def new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER,
                         json=order_body)

response = new_order(data.order_body)
print(response.status_code)
print(response.json())

def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO + str(track))
