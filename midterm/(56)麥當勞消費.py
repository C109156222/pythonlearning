set_meal = input("請選擇主餐及升級的套餐:")
large_drink = input("是否升級成大杯飲料:")
big_potato = input("是否換成大薯:")
a = [0,72,62,82,44,60]
sum = a[int(set_meal[0])]
if set_meal[1] == 'A':
    sum += 55
else:
    sum += 68
if large_drink == '是':
    sum += 7
if big_potato == '是':
    sum += 13
print("總共為%d元" %(sum))