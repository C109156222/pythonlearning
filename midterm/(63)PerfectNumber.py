n = int(input("請輸入正整數n:"))
factor_total = 0
for i in range(1,n):
    if n % i == 0:
        factor_total += i
if factor_total > n:
    print("abundant")
elif factor_total < n:
    print("deficent")
else:
    print("perfect")