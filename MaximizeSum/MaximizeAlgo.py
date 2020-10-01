lines = 3
modulo = 1000
groups = [
[2,5,4],
[3,7,8,9],
[5,5,7,8,9,10]]

new = []

for line in groups:
    new.append([x**2 % modulo for x in line])

new += [[0]]*(7-len(new))

print(new)

largest = 0

for q in new[0]:
    for w in new[1]:
        for e in new[2]:
            for r in new[3]:
                for t in new[4]:
                    for y in new[5]:
                        for u in new[6]:
                            summation = sum((q,w,e,r,t,y,u)) % modulo
                            if summation > largest:
                                largest = summation

print(largest)
