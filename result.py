
def find_order_by_id(id,orders):
    for order in orders:
        if id == order["id"]:
            return order
def close_order(id,orders):
    for order in orders:
        if (id == order["id"]) and (order["status"] == "OPEN"):
            order["status"] = "CLOSE" 
            return orders
    return "try agien!!"   
def Sales_Report(orders):
    result = sorted(orders,key=lambda o: o.get("total",0),reverse=True)
    print(f"======Sales_Report====== \ntotal orders: {len(orders)} \nMost expensive: {result[0]} \ntree Most expensive: {result[:3]}")
