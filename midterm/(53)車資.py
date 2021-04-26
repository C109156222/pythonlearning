km = float(input("路程公里數km:"))
fare = 75
if km > 1.5:
    km -= 1.5
    if km % 0.25 != 0:
        km = (km // 0.25) + 1
    else:
        km = km // 0.25
    fare += km * 5
print("所需車資為:",fare)