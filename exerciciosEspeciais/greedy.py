def min_coins(coins, amount):
    # Sort the list of coins in descending order
    coins.sort(reverse=True)
    total_coins = 0
    for coin in coins:
        # Find the number of coins of this denomination
        count = amount // coin
        amount -= count * coin
        total_coins += count
        # If we have made the exact change, break out of the loop
        if amount == 0:
            break
    return total_coins

# Example usage
coins = [1, 5, 10, 25]
amount = 63
print(f"Minimum coins needed: {min_coins(coins, amount)}")
