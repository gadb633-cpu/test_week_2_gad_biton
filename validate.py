
def val_not_empty(num):
    if num.strip():
        return True
    return False

def positive_num(num):
    if num < 0:
        return False
    return True

def val_even_num(num):
    if num % 2 == 0:
        return True
    return False

def check_if_excit(num_order):
    pass

def val_num_between_range(num):
    if num<0 or num >5:
        return False
    return True
