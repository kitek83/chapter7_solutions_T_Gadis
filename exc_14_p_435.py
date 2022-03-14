import matplotlib.pyplot as plt
def main():
    file = open('expenses.txt', 'r')
    exp = file.readlines()
    print(exp)
    expens = []
    file = open('expenses.txt', 'r')
    for ind in file:
        expens.append(ind)
    print('expense:',expens)

    values = exp
    slice_labels = ['rent','fuel','food','clothes','car installments','others']
    plt.pie(values, labels=slice_labels)

    plt.show()

main()