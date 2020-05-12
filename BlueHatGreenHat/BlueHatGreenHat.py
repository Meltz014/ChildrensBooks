from .animal import Animal, OopsError
from . import clothing

# TODO: context manager for OopsError

def main():

    try:
        elephant = Animal()
        elephant.head.place(clothing.Hat('Blue'))
        moose = Animal()
        moose.head.place(clothing.Hat('Green'))
        bear = Animal()
        bear.head.place(clothing.Hat('Red'))
        turkey = Animal()
        turkey.feet.place(clothing.Hat('Yellow'))
    except OopsError as err:
        print(err.args[0])

    try:
        elephant.torso.place(clothing.Shirt('Red'))
        bear.torso.place(clothing.Shirt('Blue'))
        moose.torso.place(clothing.Shirt('Yellow'))
        turkey.legs.place(clothing.Shirt('Green'))
    except OopsError as err:
        print(err.args[0])

    try:
        elephant.legs.place(clothing.Pants('Yellow'))
        bear.legs.place(clothing.Pants('Red'))
        moose.legs.place(clothing.Pants('Green'))
        turkey.head.place(clothing.Pants('Blue'))
    except OopsError as err:
        print(err.args[0])

    try:
        bear.back.place(clothing.Coat('Blue'))
        turkey.front.place(clothing.Coat('Green'))
    except OopsError as err:
        print(err.args[0])

    try:
        elephant.feet.place(clothing.Socks('Red'))
        turkey.hands.place(clothing.Socks('Yellow'))
    except OopsError as err:
        print(err.args[0])

    try:
        elephant.feet.place(clothing.Shoes('Green'))
        bear.feet.place(clothing.Shoes('Yellow'))
        moose.feet.place(clothing.Shoes('Blue'))
        turkey.head.place(clothing.Shoes('Red'))
    except OopsError as err:
        print(err.args[0])

    try:
        turkey.head.place(clothing.Hat('Yellow'))
        turkey.torso.place(clothing.Shirt('Green'))
        turkey.legs.place(clothing.Pants('Blue'))
        turkey.feet.place(clothing.Socks('Purple'))
        turkey.feet.place(clothing.Shoes('Red'))
        turkey.swim()
    except OopsError as err:
        print(err.args[0])
