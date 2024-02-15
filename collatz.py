import matplotlib.pyplot as plt

def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int((3*n + 1)/2)

xlist = []
ylist = []

num = input("Enter a number:")
num = int(num)

b = int(num)

while b != 1:
    a = b
    b = collatz(b)
    xlist.append(a)
    ylist.append(b)

plt.figure(num=0, dpi = 150)
plt.plot(xlist,ylist)
plt.show()