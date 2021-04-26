A = input("請輸入A的朋友:").split()
B = input("請輸入B的朋友:").split()
common_friends = 0
for i in A:
    for j in B:
        if i == j:
            common_friends += 1
            B.remove(j)
print(common_friends)