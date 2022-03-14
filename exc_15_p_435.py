import matplotlib.pyplot as plt
def main():
   file = open('fuel_price.txt', 'r')
   file2 = open('left_edges.txt', 'r')
   fuel = file.readlines()
   heights = fuel
   left_edges = file2.readlines()
   plt.bar(left_edges,heights)
   plt.show()



main()