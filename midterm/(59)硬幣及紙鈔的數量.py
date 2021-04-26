amount = int(input(''))
ans = 0
ans += amount // 100
amount %= 100
ans += amount // 50
amount %= 50
ans += amount //10
amount %= 10
ans += amount // 5
amount %= 5
ans += amount
print(ans)