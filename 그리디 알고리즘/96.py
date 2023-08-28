n, m = map(int, input().split())

result = 0
for i in range(n):
    cards = list(map(int, input().split()))
    cards.sort()
    if (result < cards[0]):
        result = cards[0]

print(result)
