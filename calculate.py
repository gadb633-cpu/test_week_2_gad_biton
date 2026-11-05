
def get_info_new_order(product_id,quantity_amout,orders:list):
    new_order = {
    "id": len(orders)+1,
    "items": [{"product_id": product_id, "quantity": quantity_amout}],
    "total": 0,
    "status": "OPEN"}
    return new_order

def get_info_product(product_id,quantity_amout,order):
    order["items"].append({"product_id": product_id, "quantity": quantity_amout})
    return order

def calculate_price(quantity_amout,product_id,products,new_order:dict):
    first_price = new_order["total"]
    for product in products:
        if product["id"] == product_id:
            first_price += product["price"] * quantity_amout
    new_order["total"] = first_price
    return new_order

def calculate_discount(new_order):
    print(f"first price:{new_order["total"]}")
    if new_order["total"] >= 300 and new_order["total"] <700:
        print(f"discount:{new_order["total"]*0.05}")
        new_order["total"] *=0.95
    elif new_order["total"] >= 700 and new_order["total"] <1500:
        print(f"discount:{new_order["total"] * 0.1}")
        new_order["total"] *=0.9
    elif new_order["total"] >= 1500:
        print(f"discount:{new_order["total"] * 0.15}")
        new_order["total"] *=0.85
    print(f"final price: {new_order["total"]}")    
    return new_order

         

            


