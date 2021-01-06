#Name: Richard Janssen
#Date: 1/5/2021
#Description: this script demonstrates how to break a loop

from math import sqrt

for i in range(1001, 0, -1):
    root = sqrt(i)

    # #This evaluates when the root is an integer
    # if root == int(root):
    #     print(root)
    #     break