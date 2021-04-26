in1 = int(input("請輸入陣列大小:"))
list1 = []
location = []
for i in range(in1):
    tmp = input("").split()
    for j in range(in1):
        list1.append(int(tmp[j]))
        location.append("(%s,%s)" %(i,j))
max1=list1
max1.sort()

a = max1[6]
b = max1[7]
c = max1[8]

t1 = list1.index(a)
t2 = list1.index(b)
t3 = list1.index(c)

print("最大值為:%d\n位置為%s,%s,%s" %(a+b+c,location[t1],location[t2],location[t3]))