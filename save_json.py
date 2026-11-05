import json
def save_order_in_json(order):
    orders = [load_from_json()]
    orders.append(order)
    with open("orders.json", "w",encoding="utf-8") as file:
        file.write(json.dumps(orders))

def load_from_json():
    with open("orders.json", "r", encoding="utf-8") as file:
        content = file.read()
        return json.loads(content)
    