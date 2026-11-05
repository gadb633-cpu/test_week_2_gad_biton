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