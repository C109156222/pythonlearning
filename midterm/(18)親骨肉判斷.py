def chkBlood(father, mother):
    if father == 'AB' or mother == 'AB':
        if father == 'O' or mother == 'O':
            return ['A','B']
        else:
            return ['A','B','AB']
    elif father == mother:
        if father == 'O':
            return ['O']
        else:
            return [father,mother]
    elif father == 'O' or mother == 'O':
        return list(set(father,mother,'O'))
    else:
        return ['A','B','O','AB']
in1 = int(input("測試的資料量:"))
for i in range(in1):
    in2 = input("").split()
    enable = chkBlood(in2[0], in2[1])
    if in2[2] in enable:
        print('yes')
    else:
        print('impossible')