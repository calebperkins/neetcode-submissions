class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        return coin_change(coins, amount)


# naive recursion
def coin_change_recursive(denominations, amount):
    def _coins_needed(a):
        if a == 0:
            return 0
        needed = [_coins_needed(a - d) for d in denominations if a >= d]
        return 1 + min(needed, default=float("inf"))

    x = _coins_needed(amount)
    return x if x < float("inf") else -1


# Using O(amount) space
def coin_change(coins, amount):
    needed = [None for _ in range(amount + 1)]
    needed[0] = 0
    for coin in coins:
        if coin <= amount:
            needed[coin] = 1

    for a in range(1, amount + 1):
        needed[a] = 1 + min((needed[a - d] for d in coins if a >= d), default=float("inf"))

    x = needed[amount]
    return x if x < float("inf") else -1
