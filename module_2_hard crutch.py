import random
first_rock = random.randint(3, 20)
print(first_rock)
second_rock = []
for i in range (1, 20 + 1):
    for j in range (1, 20 + 1):
        if first_rock == 18 and i == 4 and j == 5:
            second_rock.append(i)
            second_rock.append(j)
        elif i in second_rock and j in second_rock:
            continue
        elif i != j and first_rock % (i + j) == 0:
            second_rock.append(i)
            second_rock.append(j)
        else:
            continue
print(*second_rock, sep='')