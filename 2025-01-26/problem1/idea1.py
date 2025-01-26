# problem: https://leetcode.com/problems/find-the-winning-player-in-coin-game/
# space: O(1) | time: O(min(x, y // 4))


def winning_player(x, y):
    player = 0
    while x >= 1 and y >= 4:
        x -= 1
        y -= 4
        player = ~player
    if player == 1:
        return "Alice"
    else:
        return "Bob"
