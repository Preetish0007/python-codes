def nextCard(cards):
    if not cards:
        return None, []
    next_card = cards[0]
    new_hand = cards[1:] + [cards[0]]
    return next_card, new_hand

def check_consecutive_pairs(cards):
    for i in range(len(cards) - 1):
        if cards[i] == cards[i+1]:
            return True
    return False

# A hand of cards
cards = [1,2,2,3]

# Loop to call the function and print the top card each time
while cards:
    next_card, cards = nextCard(cards)
    print("Next card:", next_card)

    # Checking for consecutive identical pairs
    if check_consecutive_pairs(cards):
        print("Consecutive identical pair found!")
        break    

if not cards:
    print("The deck is empty.")
