
def val_not_empty(item):
    if item.strip():
        return True
    return False

def positive_num(num):
    if num < 0:
        return False
    return True

def val_even_num(num):
    if isinstance(num,float):
        return False
    return True

def check_if_excit(num_order,products):
    for product in products:
        if num_order == product["id"]:
            return False
    return True
    
def val_num_between_range(num):
    if num<0 or num >5:
        return False
    return True

def val_if_yes_or_no(enser):
    if enser in ["yes","no"]:
        return True
    return False
