#checking if the list from txt file can be loaded
file_ac = open('charge_accounts.txt', 'r')
#for acc in file_ac:
    #print(acc)
accounts = file_ac.readlines()
print('#################')
print(accounts)
for c in accounts:
    print(c)

list2 = []
for ac in accounts:
    list2.append(ac)
print('list2 is:', list2)


list = [5658845,7899887,4552135,7755684,4456878,1125456]
if 7899887 in list2:
    print('It is ok')
else:
    print('account is wrong')