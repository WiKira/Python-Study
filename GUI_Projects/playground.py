def add(*args):
    sum = 0
    for n in args:
        if str.isnumeric(str(n)):
           sum += n
    return sum

print(add(1, 2, 3))

print(add(1, 2, 3, 4, 5))

print(add(1, 2, 3, 'a'))


def calculate(**kwargs):
    print(kwargs)
    for (key, value) in kwargs.items():
        print(f"{key} = {value}")


calculate(add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.sits = kw.get("sits")


my_car = Car(make="Nissan")
print(my_car.model)

