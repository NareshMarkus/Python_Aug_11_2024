#Break
for i in [2,3,5]:
    if i == 3:
        break
    print(i)

for i in [2,3,5]:
    print(i)
    if i == 3:
        break

#Continue
for i in [2,3,5]:
    print(i)
    if i == 3:
        continue

for i in [2,3,5]:
    if i == 3:
        continue
    print(i)

#List comprehension
a = [i for i in range(1,6)]
print(a)