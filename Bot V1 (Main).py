import time

menu = {
    'burgers': {
        'bacon burger': {'name': 'Bacon Burger', 'price': 4.00, 'amount': 1},
        'smoke house': {'name': 'Smoke House Burger', 'price': 5.50, 'amount': 1},
        'crazy': {'name': 'Crazy Burger', 'price': 5.50, 'amount': 1},
        'jack daniels': {'name': 'Jack Daniels Burger', 'price': 6.00, 'amount': 1},
        'vegetarian': {'name': 'Vegetarian Burger', 'price': 5.50, 'amount': 1},
        'master burger': {'name': 'Master Burger', 'price': 8.50, 'amount': 1}
    },
    'sides': {
        'french': {'name': 'French Fries', 'price': 1.00, 'amount': 1},
        'bacon fries': {'name': 'Bacon Fries', 'price': 1.20, 'amount': 1},
        'cheese': {'name': 'Cheese Fries', 'price': 1.20, 'amount': 1},
        'master fries': {'name': 'Master Fries', 'price': 2.00, 'amount': 1}
    },
    'drinks': {
        'soda': {'name': 'Soda', 'price': 1.00, 'amount': 1},
        'water': {'name': 'Water', 'price': 1.20, 'amount': 1},
        'lemonade': {'name': 'Lemonade', 'price': 1.20, 'amount': 1},
        'beer': {'name': 'Beer', 'price': 2.00, 'amount': 1}
    }
}

specials = {
    # 'half off': {'info': "Buy Two Master Burgers And Get The Thirds Half Off"}
}

order_rules = [
    'get', 'have', 'order', 'want', 'would like'
]

removal_rules = [
    'remove', 'nevermind'
]

query_rules = [
    'how much for',
    'price of',
    'price for'
]

bill_rules = [
    'my bill', 'my order'
]

number_modifiers = {
    'a': 0, '1': 0, 'one': 0,
    '2': 1, 'two': 1,
    '3': 2, 'three': 2,
    '4': 3, 'four': 3,
    '5': 4, 'five': 4,
    '6': 5, 'six': 5,
    '7': 6, 'seven': 6,
    '8': 7, 'eight': 7,
    '9': 8, 'nine': 8,
    '10': 9, 'ten': 9
}

order = {}

bot_template = "BOT: {0}"


def print_order():
    total = 0
    print("\tYour Current Bill Is:")
    for item, info in order.items():
        print('\t\t* {} {} - {}'.format(info['amount'], info['name'], info['price'] * info['amount']))
        total = total + info['price'] * info['amount']
    print("Your Total Is: {}".format(total))


def print_menu():
    print("\n~~~~~~~~~~~~~~~~~~ M E N U ~~~~~~~~~~~~~~~~~~")
    for category, contents in menu.items():
        print("~ " + category.upper())
        for item, info in contents.items():
            print("\t* {} - ${}".format(info['name'], info['price']))


def print_specials():
    print("\n~~~~~~~~~~~~~~~ S P E C I A L S ~~~~~~~~~~~~~~~")
    if specials:
        for item, info in specials.items():
            print("* {}".format(info['info'], ))
    else:
        print("* No Specials This Week.")


def respond(message):
    message = message.lower()

    for rule in bill_rules:
        if rule in message:
            if order:
                output = ''
                print_order()
            else:
                print("You Haven't Ordered Anything")

    for rule in query_rules:
        if rule in message:
            for category, contents in menu.items():
                for item, info in contents.items():
                    if item in message:
                        print("\t* {} - ${}".format(info['name'], info['price']))

    output = 'Have Been Removed From Your Bill.'
    for rule in removal_rules:
        if rule in message:
            for category, contents in menu.items():
                for item, info in contents.items():
                    if item in message:
                        if order[item]['amount'] > 1:
                            order[item]['amount'] -= 1
                        else:
                            try:
                                del order[item]
                                output = str(info['amount']) + ' ' + info['name'] + ', ' + output
                            except KeyError:
                                output = "Item Not On The Bill"

    output = 'Have Been Added To Your Bill.'
    for rule in order_rules:
        if rule in message:
            for category, contents in menu.items():
                for item, info in contents.items():
                    if item in message:
                        if order:
                            for item2, info2 in order.items():
                                if item2 is item:
                                    order[item]['amount'] += 1
                            order.update({str(item): contents[item]})
                        else:
                            order.update({str(item): contents[item]})
                        output = str(info['amount']) + ' ' + info['name'] + ', ' + output
    return output


def send_message():
    # Print user_template including the user_message
    message = input("\nUSER: ")
    time.sleep(1)
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


print("""•••••••••••••••••••••••••••••••••••••••••••••••
           WELCOME TO MASTER BURGERS
•••••••••••••••••••••••••••••••••••••••••••••••""")
print_specials()
print_menu()
while True:
    send_message()
