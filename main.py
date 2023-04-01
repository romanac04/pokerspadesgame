cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')

def check_straight(card1, card2, card3):
    values = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 11, 'SQ': 12,
                  'SK': 13, 'SA': 14}

    card_values = sorted([values[card] for card in [card1, card2, card3]])

    if card_values[0] + 1 == card_values[1] and card_values[1] + 1 == card_values[2]:
         return max(card_values)
    else:
         return 0


def check_3ofa_kind(card1, card2, card3):
    if card1[1:] == card2[1:] == card3[1:]:
        values = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 11, 'SQ': 12,
              'SK': 13, 'SA': 14}
        return values[card1]
    else:
        return 0

def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    left_straight = check_straight(left1, left2, left3)
    right_straight = check_straight(right1, right2, right3)
    left_3ofa_kind = check_3ofa_kind(left1, left2, left3)
    right_3ofa_kind = check_3ofa_kind(right1, right2, right3)

    if left_straight > right_straight:
        return -1
    elif right_straight > left_straight:
        return 1
    else:
        return 0
    if left_3ofa_kind > right_3ofa_kind:
        return -1
    elif right_3ofa_king > left3ofaking:
        return 1
    else:
        return 0

    left_royal_flush = check_royal_flush(left1, left2, left3)
    right_royal_flush = check_royal_flush(right1, right2, right3)
    if left_royal_flush > 0 and right_royal_flush == 0:
        return -1
    elif right_royal_flush > 0 and left_royal_flush == 0:
        return 1
    if left_royal_flush > right_royal_flush:
        return -1
    elif right_royal_flush > left_royal_flush:
        return 1
    else:
        return 0