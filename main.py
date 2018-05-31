from utils import polish
from winnowing import winnow, select_min
from res_con import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    file1 = open('codes/AVLNode.java','r')
    file2 = open('codes/BSTNode.java','r')
    code1 = file1.read()
    code2 = file2.read()

    test1 = polish(code1)
    test2 = polish(code2)

    winnow1 = winnow(test1)
    winnow2 = winnow(test2)

    plt.figure("similarities")
    data = []
    labels = []
    for i in range(1, 500):
        #  res_con(a, b, num_of_data_to_choose_in_a_and_b)
        data.append(res_con(winnow1, winnow2, i))
        labels.append(i)
    data = np.array(data)
    labels = np.array(labels)
    plt.plot(labels, data)
    plt.show()

if __name__ == "__main__":
    main()