n = int(input("整數n:"))
print("整數:%d" %(n),end=" ")
cycle_lengh = 1
while n != 1:
    if n % 2 != 0:
        n = n * 3 + 1
        cycle_lengh += 1
        print(int(n),end=" ")
    else:
        n /= 2
        cycle_lengh += 1
        print(int(n),end=" ")
print("")
print("cycle lengh:",cycle_lengh)