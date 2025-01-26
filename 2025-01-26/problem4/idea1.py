def find_max_length(nums):
    m = {0: -1}
    count = maxi = 0
    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1
        if count not in m:
            m[count] = i
        else:
            maxi = max(maxi, i - m[count])
    return maxi
