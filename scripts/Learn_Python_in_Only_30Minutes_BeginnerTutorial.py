# --------Learn_Python_in_Only_30Minutes_BeginnerTutorial-------------------

# Youtube Link: https://www.youtube.com/watch?v=Ro_MScTDfU4

import math
from math import sqrt

# DataTypes

name = "Staurt"
print("Hello World " + name + "!")

text: str = "apple"
number: int = 10
decimal: float = 19.345
has_money: bool = False
cordinates: tuple = (13.24, 23.67, 34.98)
name: list = ["Stuart", "Sahil", "Alex"]
unique: set = {1, 2, 45, 67, 67, 85, 85}
print(unique)

users: dict = {"Bob": 1, "James": 2}
print(users)


# Typecasting
number: str = "100"
print(10 + int(number))

print(float("10245.256"))
a = float("10245.256")
type(a)

# Type Annotations:
age: int = 10
name: str = "Bob"

# print("Age:", age)
print("Name: " + name + "," + " Age: " + str(age))
print(f"Name: {name}, Age: {age}")


# ------Functions------------:


def add(a: float, b: float) -> float:
    # return 2a + 2b
    c = 2 * a + 2 * b
    return c


d = add(a=10, b=216)
print(d)

# print(add(a=10, b=26))


def fun() -> None:
    print("Hello")


fun()
fun()
fun()
fun()
fun()

# Loops:

for i in range(5):
    print("Hello Sahil")


names: list[str] = ["Raju", "Akankasha", "Laddu", "Mummi", "Sahil"]

for name in names:
    print(name)

####

names: list[str] = ["Raju", "Akankasha", "Laddu", "Mummi", "Sahil"]

for i in names:
    print(f"Hello: {i}")
    print("..##..")
####


# While Loop

# while True:
#     print("I Love You Sahil")  # Infinite loop


i: int = 0
while i < 3:
    print(i)
    i += 1


# -------- Comparision Operator ------------

a: int = 12
b: int = 26

print(a > b)
print(a >= b)
print(a == b)
print(a != b)


# -------- if elif ------------Simple Bot-----------------

## %%
"""
while True:
    userinput: str = input("You: ")

    # userinput: str = 'byeasd'

    if userinput == "hello":
        print("bot: hello")

    elif userinput == "how are you?":
        print("bot: I am good, how are you?")

    elif userinput == "bye":
        print("bot: Goodbye")

    else:
        print("Hi User, I could not undertood your input")
"""
## %%

# -------- exception handling ------------

# a, b = 10,15
# print(a + b)


a, b = 10, "15"

try:
    print(a + b)
except Exception as e:
    print(f"Something went wrong - {e}")

print("Continue with Program from here")

c, d = 15.5, 89.56

print(c * d)

####

## %%
a, b = 10, "15"
try:
    print(a + b)
except Exception as e:
    print(f"Something went wrong - {e}")
    print("Please enter a valid number:")

print("Continue with Program from here")

c, d = 15.5, 89.56

print(c * d)
####

## %%

## %%
a, b = 10, "15"
try:
    print(a + int(b) / 0)
except TypeError:
    print("Please enter a valid number in the form of integer or float")

except Exception as e:
    print(f"Something else went wrong - {e}")


print("Continue with Program from here")

c, d = 15.5, 89.56

print(c * d)

## %%

##-----------import------------------------


print(math.sqrt(13))
print(math.sqrt(64))

print(sqrt(121))

##-----------------------------------


##-------------Chatbot Creation--------------------------------

# %%
bot_name: str = "Sahil Chatbot:-"
print(
    f"My name is {bot_name}. How can I help you? I provide following services: \n 1. + addition \n 2. - substraction \n 3. emotional support"
)

while True:
    user_input = input("You ").lower()

    if user_input in ["hi", "hello", "namaste"]:
        print(
            f"{bot_name} Hi... how are you? How can I help you? I provide following services: \n 1. addition \n 2. substraction \n 3. emotional support"
        )

    elif user_input in ["bye", "goodbye"]:
        print(f"{bot_name}: Thank you for your visit. Come again. Bye")

    elif user_input in ("+", "addition"):
        try:
            print(
                "Sure. I can help you in addition. Please enter first number and second number:"
            )
            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))
            print(f"Addition of first number and second number is: {num1 + num2}")
        except ValueError:
            print("Plese enter a valid number.")

    elif user_input in ("-", "substraction"):
        try:
            print(
                "Sure. I can help you in substraction. Please enter first number and second number:"
            )
            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))
            print(f"substraction of first number and second number is: {num1 - num2}")
        except ValueError:
            print("Plese enter valid number")

    elif user_input in ("emotional support", "support", "help"):
        try:
            print(
                "Sure. I can help you on emotional support. Please select one from following: \n 1: Feeling lost \n 2: Feeling overthinking \n 3: Feeling unknown fear"
            )

            emotion = str(input("User's Emotion: ")).strip().lower()

            if "lost" in emotion:
                print(
                    f"Best solution for your emotion:- {emotion} - is Meditation for 15 min"
                )
            elif "overthinking" in emotion:
                print(
                    f"Best solution for your emotion:- {emotion} - is Dance for 10-15 min, followed by relaxation for 15 min"
                )
            elif "fear" in emotion:
                print(
                    f"Best solution for your emotion:- {emotion} - is belly breathing for 5 min, with emphasis on exhale"
                )
            else:
                print(f"I can not help you in this emotion - {emotion}")

        except ValueError as e:
            print(f"Something else went wrong - {e}")

    else:
        print("I could not understand your input. Please try again")


# %%
