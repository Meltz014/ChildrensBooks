from . import clothing

class OopsError(Exception):
    pass

class BodyPart():
    def __init__(self):
        self.valid_clothing = []
        self.current_clothing = []

    def place(self, article):
        if type(article) in self.valid_clothing:
            print(f'{article.color} {type(article).__name__}')
            self.current_clothing.append(article)
        else:
            raise OopsError('Oops!')

class Head(BodyPart):
    def __init__(self):
        BodyPart.__init__(self)
        self.valid_clothing = [clothing.Hat]

class Feet(BodyPart):
    def __init__(self):
        BodyPart.__init__(self)
        self.valid_clothing = [clothing.Socks, clothing.Shoes]

class Torso(BodyPart):
    def __init__(self):
        BodyPart.__init__(self)
        self.valid_clothing = [clothing.Shirt]

class Back(BodyPart):
    def __init__(self):
        BodyPart.__init__(self)
        self.valid_clothing = [clothing.Coat]

class Front(BodyPart):
    def __init__(self):
        BodyPart.__init__(self)
        self.valid_clothing = []

class Legs(BodyPart):
    def __init__(self):
        BodyPart.__init__(self)
        self.valid_clothing = [clothing.Pants]

class Hands(BodyPart):
    def __init__(self):
        self.valid_clothing = []


class Animal():

    def __init__(self):
        self.head = Head()
        self.feet = Feet()
        self.torso = Torso()
        self.back = Back()
        self.front = Front()
        self.legs = Legs()
        self.hands = Hands()

        self.parts = [self.head,
                      self.feet,
                      self.torso,
                      self.back,
                      self.front,
                      self.legs,
                      self.hands]

    def swim(self):
        for part in self.parts:
            if part.current_clothing:
                raise(OopsError('Oops!'))