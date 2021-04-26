def prime(x):
    if x > 2:
        for i in range(2,x-1):
            if x % i == 0:
                return False
        return True
    elif(x == 2):
        return True
in1 = input("請輸入正整數:")
list1 = []
for i in range(len(in1)):
    for j in range(i+1,len(in1)+1):
        if prime(int(in1[i:j])) == True:
            list1.append(in1[i:j])
if len(list1) == 0:
    print("No prime found")
else:
    list1.sort()
    print("子字串中最大的質數值為:",list1[len(list1)-1])