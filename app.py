import re

menu = {
    "ceaser salad": {"price": 1500}

}

text2 = "let me get two ceaser salads and a small coke"
text1 = "can i get a ceaser salad and a small coke"

order_rules = [
    "get (.*)",
    "have (.*)",
    "want (.*)",
    "order (.*)"
]

conjunction_rules = [
    "(.*) and (.*)",
    "(.*) with (.*)"
]

menu_modifier_rules = [
    "a (.*)", "one (.*)", "1 (.*)",
    "two (.*)", "2 (.*)"
]


def test_rules(rules, message):
    for rule in rules:
        match = re.search(rule, message)
        if match is not None:
            return match.group(1)


def test_for_conj(conjunctions, statement):
    output = []
    for rule in conjunctions:
        match = re.search(rule, statement)
        if match is not None:
            output.append(match.group(1))
            output.append(match.group(2))
            return output

# def test_for_modifiers(phrases, modifier):
#     for phrase in phrases:
#         match = re.search(modifier, phrase)
#         if match is not None:
#             output =


x = test_rules(order_rules, text1)
x = test_for_conj(conjunction_rules, x)

print(x)
# print(x.split())
# print(re.search("can i get (.*)", x).group(1))
