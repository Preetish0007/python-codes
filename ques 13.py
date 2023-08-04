cards = [1, 5, 3, 4, 2, 3, 2]

for _ in range(len(cards)):
    next_card, cards = nextCard(cards)
    print("Next card:", next_card)
#program that uses the nextCard function to check a deck of cards
    def check_for_pairs(cards):
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            return True
    return False

cards = [1, 5, 3, 4, 2, 2, 3]

if check_for_pairs(cards):
    print("Consecutive identical pair found.")
else:
    print("No consecutive identical pairs found.")