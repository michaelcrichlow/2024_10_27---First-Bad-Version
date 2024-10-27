def firstBadVersion(n: int) -> int:
    # establish first and last
    first = 1
    last = n

    while first < last:
        mid = first + (last - first) // 2

        if isBadVersion(mid) == True:
            last = mid  # the first bad version will be mid or before

        elif isBadVersion(mid) == False:
            first = mid + 1  # the first bad version must be after mid

    return first
