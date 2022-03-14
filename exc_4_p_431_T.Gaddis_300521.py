#checking the file charge_accounts.txt if the account nr is correct
def main():
    file_ac= open('accounts_list.txt.txt', 'r')
    another = 't'
    while another == 't':
        ac_num = int(input('Enter account nr:'))
        ac_num = str(ac_num)
        accounts = file_ac.readlines()

        if ac_num in accounts:
            print('Your account nr is crrect.')
        else:
            print('Your account nr is wrong.')
        another = input('Press "t", if You want to check another account nr?')


main()