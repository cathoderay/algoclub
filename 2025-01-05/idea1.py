# bubble sort
def sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break