def solution(n, lost, reserve):
    sreserve = set(reserve)-set(lost)
    slost = set(lost)-set(reserve)
    for i in sreserve:
        if i-1 in slost:
            slost.remove(i-1)
        elif i+1 in slost:
            slost.remove(i+1)
    return n-len(slost)

# 도난당했지만 여분도 있는 사람들은 제외한다
