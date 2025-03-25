def czy_palindrom(napis):

    if len(napis) <= 1:
        return True

    if napis[0] != napis[-1]:
        return False

    return czy_palindrom(napis[1:-1])


print(czy_palindrom("kajak"))  # ➝ True
print(czy_palindrom("radar"))  # ➝ True
print(czy_palindrom("python"))  # ➝ False
print(czy_palindrom("anna"))  # ➝ True
