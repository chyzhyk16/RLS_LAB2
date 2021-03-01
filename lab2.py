import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


INPUT_ARRAY = [
[0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 1, 0, 1],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],]
a = np.asarray(INPUT_ARRAY)
G = nx.DiGraph(a)


nx.draw(G, with_labels=True, font_weight='bold')

plt.show()
print(a)
G = nx.complete_graph(7)
for path in nx.all_simple_paths(G, source=0, target=3):
    print(path)

