def is_palindrome(x):
    x = str(x)
    y = str(x)[::-1]

    if x == y:
        return True
    else:
        return False
