# age = 20

# print (age == 20)
# print (age != 21)
# print (age > 17)
# print (age < 19)
# print (age >= 21)
# print (age <= 22)

age = 18
can_vote = age >= 18

#Boolean values Done

#Operators

age = 25
job =  True
adult = True
child = age <= 20
is_adult = not child

can_marry = age >= 20 and job or adult and not is_adult
print(can_marry)  # True


get_bike = age >= 25 and job
print(get_bike)  # False

get_car = age >= 20 or job
print(get_car)  # True

get_license = not job
print(get_license)  # True

score = 50
# score = score + 10

# Write:
score += 10
print(score)  # 70

result = 10 / 2
print(result)  # 2

ages = 20
if ages == 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# String Manipulation
first_name = "Alice"
last_name = "Smith"
agee = 15
full_name = first_name + " " + last_name
print(full_name)  # Alice Smith

greet = f"Hello, {first_name}! and i'm {agee} years old."
print(greet)  # Hello, Alice! and i'm 15 years old.

text = "Python is great!"
demo = " Python "
price = "$10.9999989999999"
print(text.upper())  # PYTHON IS GREAT!
print(text.lower())  # python is great!
print(price.strip("9"))  # Python
print(text.replace("great", "awesome"))  # Python is awesome!
print(price.startswith("$"))  # True
print(price.endswith("9"))  # True
print (text.find("is"))  # 7

print(text.replace("Python", "JavaScript"))

#If statements

temperature = 18

if temperature > 10:
    print("It's a warm day.")
elif temperature > 20:
    print("It's a cold day.")
else:
    print("It's a good Weather day.")


score = 50

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

agee = 20
need_id = True
weekend = True
holiday = False
sun = False

if agee >= 18 and need_id:
    print("you can do it")

if weekend or holiday:
    print ("at home and enjoy")

if not sun:
    print("go outside")

has_license = True
age = 10

if has_license:
    if age >= 18:
        print("Enter Room")
    else:
        print("need supervise")
else:
    print("I don't know")

#for loops

for i in range(1, 15):
    print(i)

name = "PYthon"

for i in name:
    print(i)

names = ["Raw", "ISI", "CIA", "FBI", "DGFI"]
for i in names:
    print(f"i hate {i}")
#////Infiniti loop//////////////
count = 0
while count < 1:
    print (f"count is {count}")
    count = count + 1
count = 0
#while #True:
    # print (f"count is {count}")
    # count = count + 1
#/////////////////////////////
#list
age = 10
name = "PYthon"
my_list = ["apple", 25, age, name, 4.33]

my_list[0]
print(my_list[1:])

my_list[0] = "Litchi"
my_list.append("Mango")
my_list.insert(3, "banana")
my_list.remove("Litchi")
# mas = my_list.pop()
del my_list[0]
print(my_list)

fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:])   # ["banana", "orange"]

numbers = [43, 343, 2, 55, 2, 222, "mango", "apple"]
print (len(numbers))
print(numbers.count(2))
print(numbers.index(55))
numbers.sort()
numbers.reverse()
print(numbers)
new = numbers.copy()
print(new)

if "litchi" in fruits:
    print("found apples")

    # Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")

if len(fruits) > 2:
    print(fruits[2])

numbers = [num for num in numbers if num != 2]
print(numbers)

# Wrong - both variables point to same list
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - changed!

# Right - make a copy
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list2)  # [1, 2, 3] - unchanged

#Dictionaries
dist = {
    "name" : "John",
    "age" : 25,
    "home" : "Dhaka",
}

dist["home"]
print(dist["name"])
print(dist.get("job", "Unknown"))

dist["passport"] = True
dist["phone"] = "iphone"
del dist["phone"]
age = dist.pop("age")
home = dist.pop("passport")
print(dist)
# dist.clear()
dist

print(dist.keys())
print(dist.values())
print(dist.items())

if "age" in dist:
    print("name found")
else:
    print("not found")

dist.update({"age": 44, "job": "loco"})
dist

lists = {
    "Sifat" : {"age": 29, "job": "frontend"},
    "sazzad": {"age" : 30, "Job": "Backend"},
    "Nabi": {"age": 20, "grade": "A"}
}
print(lists["sazzad"]["Job"])

# Wrong - lists can't be keys
bad_dict = {[1, 2]: "value"}  # TypeError!

# Right - use immutable types
good_dict = {(1, 2): "value"}  # Tuple is OK
#good_dict = {"1,2": "value"}   # String is OK
good_dict
print(good_dict[1,2])

#Tuples
point = (2,3,4)
dress = ("shirt", "pant", "cap", "t-shirt")

print(point[0])
print(dress[-3])
print(dress[0:2])

points = (2,3,4,5,"red")
x,y = points
print(x,y)

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!

# Wrong - not a tuple
single = (42)
print(type(single))  # <class 'int'>

# Right - include comma
single = (42,)
print(type(single))  # <class 'tuple'>

# Wrong - tuples are immutable
point = (3, 5)
point[0] = 4  # TypeError!

# Right - create a new tuple
point = (4, point[1])
# Or convert to list, modify, convert back
temp = list(point)
temp[0] = 4
point = tuple(temp)


#sets
scores = [33, 232, 44, 22, 33, 44, 22]
unique = set(scores)
print(unique)

colo = {"red", "jhon", 34, "blue"}

colo.add("green")
colo.remove("blue")
colo.discard("yellow")
print(colo)

if "red" in colo:
    print("red is here")

del set
del list
#ss
shorts = ["red", "jhon", "red", "bob", "Jhon", "Bob"]

uniqo = list(set(shorts))
print(uniqo)

nameo = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(nameo))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']

first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Repetition
stars = "*" * 5
print(stars)  # *****

message = "Hello"
print(len(message))  # 5

empty = ""
print(len(empty))    # 0


