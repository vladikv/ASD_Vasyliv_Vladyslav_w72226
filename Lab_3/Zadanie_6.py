def plecak_rekurencyjny(n, C, wartosci, wagi, memo={}):
    if (n, C) in memo:
        return memo[(n, C)]
    if n == 0 or C == 0:
        return 0
    if wagi[n - 1] > C:
        result = plecak_rekurencyjny(n - 1, C, wartosci, wagi, memo)
    else:
        result = max(
            plecak_rekurencyjny(n - 1, C, wartosci, wagi, memo),
            wartosci[n - 1] + plecak_rekurencyjny(n - 1, C - wagi[n - 1], wartosci, wagi, memo)
        )
    memo[(n, C)] = result
    return result