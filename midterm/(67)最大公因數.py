def gcd(n,m):
    remder = n % m
    while remder != 0:
        n = m
        m = remder
        remder = n % m
    return m

s = input("").split(",")
int_s = list(map(int, s))
maxi_gcd = 0
for i in int_s:
    for j in int_s:
        if i == j:
            continue
        else:
            if gcd(i,j) > maxi_gcd:
                maxi_gcd = gcd(i,j)
print(maxi_gcd)