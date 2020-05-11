items = [
    'Brown Bear',
    'Red Bird',
    'Yellow Duck',
    'Blue Horse',
    'Green Frog',
    'Purple Cat',
    'White Dog',
    'Black Sheep',
    'Goldfish',
    'Teacher',
    'Children',
]

class Item():
    def __init__(self, name: str):
        self.name = name

    def subj_phrase(self):
        return 'I see'

    def obj_phrase(self):
        return 'me'

    def question(self):
        return f'{self.name}, {self.name}, what do you see?'

    def answer(self, view):
        if len(view) > 1:
            viewstr = ' a ' + ', a '.join(v.name for v in view[:-1])
            viewstr += f' and a {view[-1].name}'
        else:
            if isinstance(view[0], PluralItem):
                viewstr = f' {view[0].name}'
            else:
                viewstr = f' a {view[0].name}'
        return f'{self.subj_phrase()}{viewstr} looking at {self.obj_phrase()}.'

class PluralItem(Item):
    def subj_phrase(self):
        return 'We see'

    def obj_phrase(self):
        return 'us.  That\'s what we see'

def main():
    items = [
        Item('Brown Bear'),
        Item('Red Bird'),
        Item('Yellow Duck'),
        Item('Blue Horse'),
        Item('Green Frog'),
        Item('Purple Cat'),
        Item('White Dog'),
        Item('Black Sheep'),
        Item('Goldfish'),
        Item('Teacher'),
        PluralItem('Children'),
    ]

    for (i, item) in enumerate(items):
        print(item.question())
        if i < len(items)-1:
            print(item.answer([items[i+1]]))
        else:
            print(item.answer(items[:-1]))

if __name__ == '__main__':
    main()