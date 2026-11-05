from shaw_menu import*
from inputs import *
from result import *
from validate import *
from calculate import*
from save_json import*


products = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}
]

def main():
    while True:
        shaw_menu()
        choice = get_num("Choose option")
        if val_num_between_range(choice) == False:
            print("out of range!!")
            continue
        if choice ==1:
            count = 0
            while True:
                product_id = get_num("enter product id")
                order_quantity = get_num("enter quantity order")
                orders = load_from_json()
                if count ==0:
                    new_order = get_info_new_order(product_id,order_quantity,orders)
                    new_order_with_price = calculate_price(order_quantity,product_id,products,new_order)
                else:
                    add_product = get_info_product(product_id,order_quantity,new_order)
                    new_order_with_fue_products = calculate_price(order_quantity,product_id,products,add_product)
                enser = get_enser()
                if enser == "yes":
                    count +=1
                    continue
                if enser =="no":
                    if count ==0:
                        price_with_discount = calculate_discount(new_order_with_price)
                        save_order_in_json(price_with_discount)
                        break
                    else:
                        price_with_discount = calculate_discount(new_order_with_fue_products)
                        save_order_in_json(price_with_discount)
                        break
        if choice ==2:
            all_orders = load_from_json()
            print(all_orders)
        if choice ==3:
            order_id = get_num("enter order id")
            all_orders = load_from_json()
            print(find_order_by_id(order_id,all_orders))
        if choice ==4:
            order_id = get_num("enter order id")
            all_orders = load_from_json()
            status = close_order(order_id,all_orders)
            if status =="try agien!!":
                print(status)
                continue
            save_order_in_json(status)
        if choice ==5:
            pass
        if choice ==0:
            break
main()        