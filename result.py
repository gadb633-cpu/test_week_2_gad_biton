
def find_order_by_id(id,orders):
    for order in orders:
        if id == order["id"]:
            return order
def close_order(id,orders):
    for order in orders:
        if id == order["id"] and order["status"] == "OPEN":
            order["status"] = "CLOSE" 
            return order
    return "try agien!!"   
