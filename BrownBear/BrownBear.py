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
    """Simulates each item's name, question, and answer based on list position.

    Note:
        Any mention of 'item' is in reference to the current iteration's
        animal or person(s) e.g. 'Brown Bear'.

    Args:
        name (str): Name of current item in the list, 'items'.
    """
    def __init__(self, name: str):
        self.name = name

    def subj_phrase(self):
        return 'I see'

    def obj_phrase(self):
        return 'me'

    def question(self):
        return f'{self.name}, {self.name}, what do you see?'

    def answer(self, view):
        """Prints the current item's answer to question().

        Args:
            view (str): Name of what the current item sees.

        Returns:
            An f-string, dependent on whether number of animals/people in
            the current item's view is one or more than one.
        """
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
    """Handles the plural Item 'Children' and its required pronouns."""
    def subj_phrase(self):
        return 'We see'

    def obj_phrase(self):
        return 'us.  That\'s what we see'

def main():
    """Instantiates items and prints the determined question and answer."""
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
