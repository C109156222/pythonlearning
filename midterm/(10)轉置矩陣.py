in1 = input("輸入N及M為:")
n = int(in1[0])
m = int(in1[2])
r = 1
row = []
while int(in1[0]) != 0:
    in1 = input("輸入矩陣數值第"+ str(r) +"列為:")
    row.append(in1)
    r += 1
for i in range(len(row)-1):
    row[i] = row[i].split(" ")
sol = []
r = 1
for j in range(m):
    tmp = ""
    for u in range(n):
        tmp += row[u][j] + " "
    print("輸出矩陣數值第" + str(r) + "列為:" + tmp)
    r += 1