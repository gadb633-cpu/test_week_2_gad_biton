
def get_num(msg):
    try:
        num = int(input(f"{msg}:"))
        return num
    except ValueError:
        return "is not num ,try agein !!"
    