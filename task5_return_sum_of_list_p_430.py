#this program showing function return the
#sume of list value
def main():
    nums = [2,3,4,5,6,7,8,9]
    sum = get_vals(nums)
    print('Sum of values in list nums is:',sum)

def get_vals(vals):
    total = 0
    for num in vals:
        total +=num
    return total

main()