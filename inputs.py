from validate import*
def get_num(msg):
    while True:
        try:
            num = int(input(f"{msg}:"))
            if val_even_num(num) == False:
                print("is not even,try agien!!")
                continue
            if positive_num(num) == False:
                print("is not positive num,try agien!!")
                continue
            return num
        except ValueError:
            print("is not num ,try agein !!")
            continue
def get_enser():
    while True:
            enser = input("you want to coutinue [yes,no] ?: ").strip().lower()  
            if val_if_yes_or_no(enser) == False or val_not_empty(enser) == False:
                print("jast yes or no")
                continue
            return enser
            