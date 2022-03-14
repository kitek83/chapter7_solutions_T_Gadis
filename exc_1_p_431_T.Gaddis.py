#prviding the value of sales for each day of week and saving it in the list
week = [0] * 7
print(week)
count = 0
index = 0
for day in week:
    count += 1
    value = float(input('Enter value of sale from day nr'+ str(count) + ':'))
    week[index] = value
    index += 1
print('The values from sale for each day of the week are in the list:')
print(week)
#calculating weekly sale value by list
print('-----------------')
total = 0
for val in week:
    total += val
print('Weekly sale is:', total)