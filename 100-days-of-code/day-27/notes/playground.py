def add(*args): #Accept any number of arguments -> args is a tuple
    # return sum(args)
    total = 0
    for n in args: #Loop through all of the arguments
        total += n
    return total

print(add(3,9,1))
print(add(1,2,3,4))
print(add(1,2,3,8,6,11))


def calculate(n, **kwargs): #unlimited key words arguments -> dictionary
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"] if make doesnt have a value -> exception
        # self.model = kwargs["model"]
        self.make = kwargs.get("make") # if make doesnt have a value -> self.make is none
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.make, my_car.model, my_car.colour, my_car.seats)
