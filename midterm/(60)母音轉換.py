in1 = input("輸入一串小寫英文:")
vowel = ['a','e','i','o','u']
for i in range(len(in1)):
    for j in vowel:
        if in1[i] == j:
            in1.replace(in1[i],".")
print(in1)