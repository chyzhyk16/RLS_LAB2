import numpy as np
import networkx as nx

INPUT_ARRAY = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], ]

STARTING_ELEMENT = [1]

END_ELEMENT = [7, 8]


def get_path_list(graph):
    l = []
    for st_el in STARTING_ELEMENT:
        for end_el in END_ELEMENT:
            for path in nx.all_simple_paths(graph, source=st_el - 1, target=end_el - 1):
                l.append(path)
    return l


def get_state_list(path_list):
    sl = []
    for path in path_list:
        l = []
        for i in range(len(INPUT_ARRAY)):
            if i in path:
                l.append(1)
            else:
                l.append(0)
        sl.append(l)
    return sl


def lab2():
    a = np.asarray(INPUT_ARRAY)
    G = nx.DiGraph(a)

    path_list = get_path_list(G)

    print(len(path_list))
    print(path_list)
    print(get_state_list(path_list))


if __name__ == '__main__':
    lab2()
