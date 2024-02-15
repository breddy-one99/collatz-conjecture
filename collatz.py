import matplotlib.pyplot as plt
import numpy as np

def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int((3*n + 1)/2)

def plot_collatz(b):
    ylist = []
    while b != 1:
        ylist.append(b)
        b = collatz(b)
    xlist = range(1, len(ylist) + 1)  # Generate xlist based on the length of ylist
    plt.plot(xlist, ylist)

num = input("Enter a number:")
b = int(num)

# for b in range(1,27):
#     plot_collatz(b)

plot_collatz(b)
plt.tight_layout()
plt.show()