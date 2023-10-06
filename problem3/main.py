def playing_domino(cards, deck):
    valid_moves = []

    for card in cards:
        if deck[0] in card or deck[1] in card:
            valid_moves.append(card)

    if not valid_moves:
        return []
    
    max_sum = 0
    best_move = []
    for move in valid_moves:
        move_sum = sum(move)
        if move_sum > max_sum:
            max_sum = move_sum
            best_move = move

    return best_move


if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []