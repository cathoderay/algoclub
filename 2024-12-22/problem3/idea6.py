def solve(x):
    if len(x) == 0:
        return True

    return x[0] == x[-1] and solve(x[1:-1])



def is_palindrome(x):
    return solve(str(x))
