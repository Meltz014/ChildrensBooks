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

# TODO: object oriented solution.  need to implement plural flag

def ask(item):
    return f'{item}, {item}, what do you see?'

def answer(next_item):
    return f'I see a {next_item}, looking at me.'

def main():
    for (i, item) in enumerate(items):
        if i > 0:
            print(answer(item))

        print(ask(item))

    print(f'We see a {", a ".join(items[:-2])} and a {items[-1]} looking at us.\nThat\'s what we see.')

main()