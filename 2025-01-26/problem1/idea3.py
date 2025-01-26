def winning_player(x, y):
    return "Alice" if min(x, y // 4) % 2 else "Bob"
