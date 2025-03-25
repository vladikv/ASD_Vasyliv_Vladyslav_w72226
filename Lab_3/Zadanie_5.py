def plecak(n, C, wartosci, wagi):
    dp = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(C + 1):
            if wagi[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], wartosci[i - 1] + dp[i - 1][j - wagi[i - 1]])
    return dp[n][C]