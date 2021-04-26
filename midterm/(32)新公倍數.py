def test_mult(a):
    return a % 2 == 0 and a % 11 == 0

def test_divide(a):
    return a % 5 != 0 and a % 7 != 0

in1 = int(input("輸入一正整數:"))
if test_mult(in1) and test_divide(in1):
    print("%d為新公倍數?:Yes" %(in1))
else:
    print("%d為新公倍數?:No" %(in1))