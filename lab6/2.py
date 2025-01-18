from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinList = [0] * (amount + 1)

        for i in range(1, amount + 1):
            minCoin = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    minCoin = min(minCoin, coinList[i - coin] + 1)
            coinList[i] = minCoin

        print(coinList)
        return coinList[amount] if coinList[amount] != float('inf') else -1
    
coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))