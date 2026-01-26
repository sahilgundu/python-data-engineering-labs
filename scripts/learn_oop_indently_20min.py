# --------learn_oop_indently_20min------------------------

# Youtube Link: https://www.youtube.com/watch?v=rLyYb7BFgQI

# Chatgpt Study chat link: https://chatgpt.com/g/g-p-689e71766efc8191bb566fc7a721c266-python-30-lpa/c/69692493-cef8-832f-aea1-1989b9768c12


# %%


class Microwave: ...


smeg: Microwave = Microwave()

print(smeg)  # Printing address of object (smeg) of class Microwave


# %%
class Microwave:
    def __init__(
        self, brand: str, power_rating: str
    ) -> (
        None
    ):  # function __init__ can be used to initialize class, we can use any word instead of self, like this, s, d etc.
        self.brand = brand
        self.power_rating = power_rating


smeg: Microwave = Microwave(brand="SMEG", power_rating="B")

print(smeg)
print(smeg.brand)
print(smeg.power_rating)


bosch: Microwave = Microwave(brand="BOSCH", power_rating="D")

print(bosch)
print(bosch.brand)
print(bosch.power_rating)


# %%
# Practice:-


class Microwave: ...


s = Microwave()
print(s)

# %%
# Practice:-


class Microwave1:
    def __init__(self, brand: str, intensity: str) -> None:
        self.brand = brand
        self.intensity = intensity


s = Microwave1(brand="Cogni", intensity="C1")
print(s)
print(f"Brand names is: {s.brand} & intensity of this piece is: {s.intensity}")

r = Microwave1(brand="Delooite", intensity="C5")
print(r)
print(f"Brand name is {r.brand} & intensity of this piece is {r.intensity}")
print(f"Brand name is {s.brand} & intensity of this piece is {r.intensity}")


# %%
# ----------------Methods-----------------------------:

# ----------Problem Statement--------------------------:
"""
    Start Microsoft, run it for input seconds and it should be turned off after every successful run.
"""


class Microwave2:
    def __init__(self, brand: str, power_setting: str) -> None:
        self.turned_on: bool = False
        self.brand = brand
        print(
            f"This brand is {self.brand} & Current status of running is {self.turned_on}"
        )

    def turn_on(self):
        if not self.turned_on:
            self.turned_on: bool = True
            print(f"This Microwave {self.brand} is turned on now")
        else:
            print(f"This Microwave {self.brand} is already turned on.")

    def turn_off(self):
        if self.turned_on:
            self.turned_on: bool = False
            print(f"This Microwave {self.brand} is turned off now")
        else:
            print(f"This Microwave {self.brand} is already turned off.")

    def run(self, duration_seconds: int) -> None:
        if not self.turned_on:
            print(
                f"Microwave {self.brand} is turned off at the moment. To run it, we must first turn on it. Should I turn on {self.brand} microwave? Please reply Yes or No."
            )
            user_input = input("Yes or No: ").lower()

            if user_input == "yes":
                self.turn_on()
                print(
                    f"{self.brand} microwave is running for {duration_seconds} seconds"
                )
                print(f"Duration of {duration_seconds} seconds is completed.")
                self.turn_off()

            elif user_input == "no":
                print(
                    f"Okay, we are keeping microwave {self.brand} turned off as it is"
                )

            else:
                print("Invalid input by user")

        elif self.turned_on:
            print(f"{self.brand} microwave is running for {duration_seconds} seconds")
            print(f"Duration of {duration_seconds} seconds is completed.")
            self.turned_on = False
            print(f"Microwave {self.brand} is turned off now.")


b: Microwave2 = Microwave2(brand="Bolt", power_setting="B12")

b.turn_on()

b.run(180)

b.turn_off()

b.run(1200)


# %%
# ------------------------- Dunder Methods (Double Underscore Method) ----------------------


class Microwave3:
    def __init__(self, brand: str, power_setting: str) -> None:
        self.turned_on: bool = False
        self.brand = brand
        self.power_setting = power_setting

        print(f"This brand is {self.brand}")

    # def __add__(self1, other1):
    #     return f'{self1.brand} **&&++ Use of Dunder method __add__ ++**&& {other1 .brand}'

    def __add__(self, other):
        return f"{self.brand} **&&++ Use of Dunder method __add__ ++**&& {other .brand}"

    def __mul__(self, other):
        return (
            f"This is dunder method __mul__(): {self.brand} **** {other.power_setting}"
        )

    def __str__(self) -> str:
        return "This is the demo of dunder method __str__ which return str upon trying to print class instance, instead of just memory of class instance"

    def __repr__(self) -> str:
        return (
            "This is demo of Dunder method __repr__() which return str upon trying to print class instance, \n"
            "but with variables etc like :- This is a {self.brand} \n"
            "& power setting here is {self.power_setting}"
        )


b: Microwave3 = Microwave3(brand="Bolt", power_setting="B12")

t: Microwave3 = Microwave3(brand="Tata", power_setting="T14")


# result = b.__add__(t)     # This is actual way of calling dunder method __add__() using symbol '+'.
# print(result)

print(type(b + t))

print(b + t)

print(b * t)

print(b)  # calls __str__()

print(t)  # calls __str__()

print(repr(t))  # calls __repr__()

# %%
