# import re
#
# menu_modifier_rules = [
#     "(a) (.*)", "(one) (.*)", "(1) (.*)",
#     "(two) (.*)", "(2) (.*)"
# ]
#
# x = 'a ceaser salad'
#
# match = re.search("(a) (.*)", x)
# print(match.group(1))
# print(match.group(2))
# print(match.group(0))

menu = [
    "ceaser salad",
    "small coke",
    "chicken"
]

mess = "can i get a small coke and two ceaser salad"

# mess = mess.lower().split()
while True:
    for item in menu:
        if item in mess:
            print(f"YES!!! {item}")
            continue
        else:
            print("NO!!!")
    break
