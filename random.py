import random

cards = ["jack", "queen", "king", "ace", 
         "two", "three", "four", "five", 
         "six", "seven", "eight", "nine", "ten"]

def main():
    print("Welcome to counting cards!")


def card_value(card):
    values = {
        "jack": -1, "queen": -1, "king": -1, "ace": -1,
        "two": 1, "three": 1, "four": 1, "five": 1, "six": 1,
        "seven": 0, "eight": 0, "nine": 0, "ten": -1
    }
    return values.get(card, 0)

def evaluate_cards():
    selected_cards = random.choices(cards, k=3)
    for card in selected_cards:
        print(f"Card: {card}, Value: {card_value(card)}")

main()
evaluate_cards()
# print the card count, eg. sum of card values
print(f"Card count: {sum(card_value(card) for card in random.choices(cards, k=3))}")
