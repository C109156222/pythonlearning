def revStr(a_str):
    return a_str == a_str[::-1]
def strSum(a_str):
    sum1 = 0
    for i in a_str:
        sum1 += int(i)
    return sum1

in1 = input("輸入整屬數列(end結束):")
sum1 = strSum(in1)
ans = ""

for i in range(len(in1)-2):
    for j in range(len(in1)-1,i-1,-1):
        t_str = in1[i:j+1]
        if revStr(t_str):
            if len(t_str) > len(ans):
                ans = t_str
                continue
            if len(t_str) == len(ans):
                if strSum(t_str) < strSum(ans):
                    ans = t_str

print(ans)