from math import inf


def merge(nums1, m, nums2, n):
    a = nums1[:m] + [inf]
    b = nums2[:n] + [inf]
    pa = pb = 0
    c = []
    for i in range(m + n):
        if a[pa] <= b[pb]:
            c.append(a[pa]); pa += 1
        else:
            c.append(b[pb]); pb += 1
    nums1[:] = c[:]
