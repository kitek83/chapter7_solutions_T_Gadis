#entering 20 numbers to the list
def main():
    nums = [0] * 20
    index = 0
    count = 0
    for num in nums:
        count += 1
        nums[index] = float(input('Enter number nr ' + str(count) + ':'))
        index += 1
    print('List nums is:', nums)
#showing the lowest number:
    print('---------------------')
    print('The lowest number from the list is:',min(nums))
    print('----------------------------')
    print('The highest number in the list:', max(nums))
    total = 0
    for num in nums:
        total += num
    print('Total value of all numbers is:', total)
#count average of the numbers from the list
    average = total / len(nums)
    print('The average of the numbers from the list is:', format(average,'.2f'))



main()