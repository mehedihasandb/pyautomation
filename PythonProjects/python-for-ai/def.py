def greet():
    print("Hello")
    print("Hello Again!!")
    pass

greet() 

def say_mesulan():
    print("Hello men")
    print("Hello World")
    print("Hello People")

say_mesulan()

def check_temp():
    temp = 25
    if temp > 30:
        print("It's normal")
    else:
        print("it' hot")

check_temp()

def price_list():
    price = 100
    tex = price * 0.10
    print(f"total: {price + tex}")
price_list()
# print(price)

discount_rate = 0.15
def apply_dis(price):
    discount = price * discount_rate
    return price - discount

result = apply_dis(100)
print(result)

counter = 0
def incre():
    global counter
    counter += 1

incre()
incre()
print(counter)

alls = 0
def all_data(amount):
    global alls
    alls += amount
alls

def ad_amount(crrent_total, amount):
    return crrent_total + amount

total = 0

total = ad_amount(total, 10)
total = ad_amount(total, 20)
total
