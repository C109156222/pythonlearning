import math
a = int(input(""))
b = int(input(""))
c = int(input(""))
if b*b - 4*a*c > 0:
    print(int((-b + math.sqrt(b*b - 4*a*c)) / (2*a)))
    print(int((-b - math.sqrt(b*b - 4*a*c)) / (2*a)))
elif b*b - 4*a*c == 0:
    print(int(-b/(2*a)))
else:
    print(0)