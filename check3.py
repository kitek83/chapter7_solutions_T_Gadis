file = open('charge_accounts.txt','r')
#print(file.read())
accounts = file.readlines()

print(accounts)
print('------------------')
if '4456878' in accounts:
    print('ok')
else:
    print('Wrong')
print('----------------')
index = 0
acc = str(int(input('Enter nr of your account:')))
#acc = 4456878
while index < len(accounts):
    if accounts[index] == acc:
        print('all ok')
    else:
        print('account is wrong')
    index += 1

