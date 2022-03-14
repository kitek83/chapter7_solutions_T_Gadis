weeks = [0] * 7
index = 0
c = 0
for day in weeks:
    c += 1
    weeks[index] = float(input(str(c) + 'Enter sale from today:'))
    index += 1
print(weeks)
