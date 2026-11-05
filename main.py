from shaw_menu import*
from inputs import *
from result import *
from validate import *

products = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}
]

order = {
    "id": 1,
    "items": [{"product_id": 1, "quantity": 2},
              {"product_id": 3, "quantity": 1}],
    "total": 1026.0,
    "status": "OPEN"
}


def main():
    while True:
        shaw_menu()
        choice = get_num("Choose option")
        if val_num_between_range(choice) == False:
            print("out of range!!")
            continue
        if choice ==1:
            while True:
                order_id = get_num("enter order id")
                order_quantity = get_num("enter quantity order")
        if choice ==2:
            pass
        if choice ==3:
            pass
        if choice ==4:
            pass
        if choice ==5:
            pass
        if choice ==0:
            break
main()        