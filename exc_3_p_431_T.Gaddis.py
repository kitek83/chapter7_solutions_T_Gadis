#writing in list rainfall information for each month
def main():
    months = [0] * 12
    index = 0
    count = 0
    for month in months:
        count += 1

        months[index] = float(input('Enter rainfall information for month nr' + str(count) + ':'))
        index += 1
    print('Rainfall info for 12 months is:',months)
#calculating total amount of the rainfall during tha year
    total = 0
    for val in months:
        total += val
    print('-------------------------------')
    print('Tota early rainfall is:', total)
#calc monthly averaage precipitaion
    average = total / len(months)
    print('Monthly average precipitaion is:',format(average,'.2f'))
#calc the lowest precipitaion from the year
    print('---------------------')
    print('The lowest value of rainfall from the year is',min(months))
#calc the highest precipitaion from the year
    print('----------------------------------')
    print('The highest precipitaion from the year is:', max(months))


main()