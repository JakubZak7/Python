def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inches(n):
    return n/2.54

def inches_to_cm(n):
    return n * 2.54

def feets_to_cm(n):
    return n* 30.48

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'200cm = {cm_to_inches(200)}inches')
    print(f'15 inches = {inches_to_cm(15)}cm')
    print(f'6.4 feets = {feets_to_cm(6.4)}cm')