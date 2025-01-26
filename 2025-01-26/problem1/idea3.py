# problem: https://leetcode.com/problems/find-the-winning-player-in-coin-game/
# space: O(1) | time: O(1)


def winning_player(x, y):
    return "Alice" if min(x, y // 4) % 2 else "Bob"
