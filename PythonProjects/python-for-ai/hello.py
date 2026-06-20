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
price = "$10.99"
print(text.upper())  # PYTHON IS GREAT!
print(text.lower())  # python is great!
print(demo.strip())  # Python
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
while #True:
    # print (f"count is {count}")
    # count = count + 1
#/////////////////////////////
#list

my_list = ["apple", 25, age, name, 4.33]

my_list[0]

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


