in1 = int(input(""))
for i in range(in1):
    sequence = []
    for j in range(4):
        sequence.append(int(input("")))
    if sequence[1] - sequence[0] == sequence[2] - sequence[1]:
        print(sequence[0],sequence[1],sequence[2],sequence[3],sequence[3] + sequence[2] - sequence[1])
        print("此為等差數列")
    else:
        print(sequence[0],sequence[1],sequence[2],sequence[3],sequence[3] * (sequence[2] / sequence[1]))
        print("此為等比數列")
