# 주어진 배열을 정렬하여 이웃한 숫자와의 갭 차이가 제일 큰 수를 리턴하시오
# ex)
# max_gap ([13,10,5,2,9]) ==> return (4)
# 9 - 5 = 4
#
# max_gap ([-3,-27,-4,-2]) ==> return (23)
# |-4- (-27) | = 23
#
# max_gap ([-7,-42,-809,-14,-12]) ==> return (767)
# | -809- (-42) | = 767
#
# max_gap ([-54,37,0,64,640,0,-15]) ==> return (576)
# | 64 - 640 | = 576

from more_itertools import windowed


def max_gap(lst):
<<<<<<< HEAD
    lst.sort()
    mmax = -987654321
    for i in range(len(lst)-1):
        gap = abs(lst[i]-lst[i+1])
        if mmax < gap:
            mmax = gap
    return mmax

print(max_gap ([13,10,5,2,9]))
print(max_gap ([-3,-27,-4,-2]))
print(max_gap ([-7,-42,-809,-14,-12]))
print(max_gap ([-54,37,0,64,640,0,-15]))
=======
    return max(map(lambda x: x[1] - x[0], list(windowed(sorted(lst), n=2))))
>>>>>>> upstream/main
