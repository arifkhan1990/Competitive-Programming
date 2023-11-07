def smartInterval(intervals, n):
    st = [0]*n
    ed = [0]*n
    for i in range(n):
        st[i] = [intervals[i][0], i]
        ed[i] = [intervals[i][1], i]
    
    st.sort()
    ed.sort()

    ans = [-1] * n
    i, j = 0, 0

    while i < n and j < n:
        if st[i][0] >= ed[j][0]:
            idx = ed[j][1]
            ans[idx] = st[i][1]
            j += 1
        else:
            i += 1
    return ans