in1 = input("輸入矩陣的維度:").split()
a_int = []
for i in range(int(in1[0])):
    in2 = input("").split()
    for j in range(len(in2)):
        a_int.append(int(in2[j]))
b_int = []
for i in range(int(in1[0])):
    in2 = input("").split()
    for j in range(len(in2)):
        b_int.append(int(in2[j]))
count = 0
for i in range(int(in1[0])):
    for j in range(int(in1[1])):
        print(a_int[count]*b_int[count],end=" ")
        count += 1
    print("")