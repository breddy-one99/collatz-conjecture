import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:

    def __init__(self):

        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int((3*n + 1)/2)

G = GraphVisualization()

num = input("Enter a number:")
num = int(num)

b = int(num)

while b != 1:
    a = b
    b = collatz(b)
    G.addEdge(a, b)

G.visualize() 