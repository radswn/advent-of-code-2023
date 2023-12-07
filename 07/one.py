import functools

card_order = {c: i for i, c in enumerate(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])}


def compare(item1, item2):
    hand1, hand2 = item1[0], item2[0]

    hand_summary_1 = {card: 0 for card in hand1}
    hand_summary_2 = {card: 0 for card in hand2}

    first_higher_card = 0

    for card1, card2 in zip(hand1, hand2):
        hand_summary_1[card1] += 1
        hand_summary_2[card2] += 1
        
        if card1 != card2 and first_higher_card == 0:
            first_higher_card = card_order[card2] - card_order[card1]

    type_1 = get_hand_type(hand_summary_1)
    type_2 = get_hand_type(hand_summary_2)

    if type_1 != type_2:
        return type_1 - type_2

    return first_higher_card


def get_hand_type(hand_summary: dict):
    card_counts = sorted(list(hand_summary.values()))
    
    if card_counts == [5]:
        return 7
    
    if card_counts == [1, 4]:
        return 6
    
    if card_counts == [2, 3]:
        return 5
    
    if card_counts == [1, 1, 3]:
        return 4
    
    if card_counts == [1, 2, 2]:
        return 3
    
    if card_counts == [1, 1, 1, 2]:
        return 2
    
    return 1


with open("07/input.txt", "r") as f:
    lines = f.readlines()

hands = []

for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    
    
    hands.append((hand, bid))

hands.sort(key=functools.cmp_to_key(compare))

result = sum([bid *(i+1) for i, (_, bid) in enumerate(hands)])

print(result)
