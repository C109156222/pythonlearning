list1 = []
for i in range(1,11):
    list1.append(int(input("請輸入第%d個數字:" %(i))))
list1.sort()
print("最大的3個數字為:",list1[9],list1[8],list1[7])
print("最小的3個數字為:",list1[2],list1[1],list1[0])