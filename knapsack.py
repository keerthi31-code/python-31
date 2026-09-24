def knapsack(weights, values, capacity):

    n = len(weights)

    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):

        weight = weights[i - 1]
        value = values[i - 1]

        for w in range(1, capacity + 1):

            if weight <= w:

                dp[i][w] = max(
                    dp[i - 1][w],
                    value + dp[i - 1][w - weight]
                )

            else:

                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = [1, 2, 3]
values = [10, 15, 40]

capacity = 5

print(knapsack(weights, values, capacity))
print("keerthi")