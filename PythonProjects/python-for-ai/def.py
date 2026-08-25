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

def add_numbers(a, b):
    return a + b
money = add_numbers(10, 20)
print(money)
result = add_numbers(1100, 2300)
print(result)


def cal_area(width, height):
    area = width * height 
    return area 

room_area = cal_area(100, 400)
print (f"room size: {room_area}");


def double(numbers):
    return numbers * 5

result = double(5)
total = double(8) + double(10) 
print(double(7))

if double(7) < 10:
    print ("Big Brain!")

def min_bum(number):
    return min(number), max(number)
mini, maxi =  min_bum([23, 124, 11, 34])

print (f"{mini}, {maxi}")

def greeting_print(name):
    print(f"Hello {name}")

def greeting_return(name):
    return f"Hello {name}" 

message = greeting_print("Loco")
print(message)

message = greeting_return("Loco")
print(message.upper())