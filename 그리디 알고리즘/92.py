n, m, k = map(int, input().split())
data = list(map(int, input().split()))


data.sort()
first = data[n-1]
second = data[n-2]

result = 0

# 단순 그리디
# 문제점은 M의 크기가 커지면 시간 초과 판정.
# while m > 0:
#    if (m >= k):
#        result = result + k * first
#        m = m - k
#    else:
#        result = result + m * first
#        m = 0
#
#    if (m > 0):
#        result += second
#        m -= 1

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result += count * first
result += (m - count) * second

print(result)
