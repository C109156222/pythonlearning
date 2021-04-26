def prime_number(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

in1 = int(input("請輸入第一個要判斷的數字:"))
in2 = int(input("請輸入第二個要判斷的數字:"))
if prime_number(in1) and prime_number(in2) and in2 - in2 == 0:
    print("Y")
else:
    print("N")