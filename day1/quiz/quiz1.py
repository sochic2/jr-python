# 주어진 숫자를 10으로 나누어 나머지가 0인 가장 가까운 숫자를 반환합니다.
#
# Example input:
#
# 22
# 25
# 37
# Expected output:
#
# 20
# 30
# 40

def closest_multiple_10(i):
    if i%10 >= 5:
        return i//10*10+10
    else:
        return i//10*10

print(closest_multiple_10(22))
print(closest_multiple_10(25))
print(closest_multiple_10(37))
