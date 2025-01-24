

def merge(nums1, m, nums2, n):
    p1 = p2 = 0
    for i in range(m + n):
        if p1 - p2 >= m:
            for j in range(p2, n):
                nums1[p1] = nums2[j]; p1 += 1
            return
        elif p2 < n and nums2[p2] < nums1[p1]:
            for j in range(m + n - 1, i-1, -1):
                nums1[j] = nums1[j-1]
            nums1[i] = nums2[p2]; p2 += 1
        p1 += 1
