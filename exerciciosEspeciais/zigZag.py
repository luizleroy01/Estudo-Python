a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]
    
    st = mid + 1
    ed = n - 1
    print(a[ed])
    while st <= ed:
        temp = a[ed]
        a[ed] = a[st]
        a[st] = temp
        st = st + 1
        ed = ed + 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end =' ')
    return