import numpy as np
import networkx as nx
import itertools as it

INPUT_ARRAY = [
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0], ]

PROBABILITY_ARRAY = [0.05, 0.96, 0.64, 0.84, 0.09, 0.65, 0.43, 0.22, 0.71]

STARTING_ELEMENT = [1, 2]

END_ELEMENT = [8, 9]


def values_check():
    if not INPUT_ARRAY or not INPUT_ARRAY[0]:
        print('INPUT_ARRAY is empty')
        return False
    if len(INPUT_ARRAY) != len(INPUT_ARRAY[0]):
        print('INPUT_ARRAY must be NxN')
        return False
    try:
        if not list(np.unique(np.asarray(INPUT_ARRAY))) == [0, 1]:
            print('INPUT_ARRAY values must be 0 or 1')
            return False
    except:
        print('INPUT_ARRAY values must be 0 or 1')
        return False
    if not PROBABILITY_ARRAY:
        print('PROBABILITY_ARRAY is empty')
        return False
    if len(PROBABILITY_ARRAY) != len(INPUT_ARRAY):
        print('PROBABILITY_ARRAY must be 1xN')
        return False
    try:
        if max(PROBABILITY_ARRAY) > 1 or min(PROBABILITY_ARRAY) < 0:
            print('PROBABILITY_ARRAY values must be between 0 and 1')
            return False
    except:
        print('PROBABILITY_ARRAY values must be between 0 and 1')
        return False
    if not STARTING_ELEMENT:
        print('STARTING_ELEMENT is empty')
        return False
    if len(STARTING_ELEMENT) > len(INPUT_ARRAY):
        print('STARTING_ELEMENT must be 1x(1,N)')
        return False
    try:
        if min(STARTING_ELEMENT) < 1:
            print('STARTING_ELEMENT values must be 1 or bigger')
            return False
    except:
        print('STARTING_ELEMENT values must be 1 or bigger')
        return False
    if not END_ELEMENT:
        print('END_ELEMENT is empty')
        return False
    if len(END_ELEMENT) > len(INPUT_ARRAY):
        print('END_ELEMENT must be 1x(1,N)')
        return False
    try:
        if min(END_ELEMENT) < 1 or max(END_ELEMENT) > len(INPUT_ARRAY):
            print('END_ELEMENT values must be from 1 to N')
            return False
    except:
        print('END_ELEMENT values must be from 1 to N')
        return False
    return True


def get_path_list(graph):
    l = []
    for st_el in STARTING_ELEMENT:
        for end_el in END_ELEMENT:
            for path in nx.all_simple_paths(graph, source=st_el - 1, target=end_el - 1):
                l.append(path)
    return l


def get_state_list(path_list):
    working_states = []
    all_states = [list(x) for x in it.product((0, 1), repeat=len(INPUT_ARRAY))]
    for state in all_states:
        for path in path_list:
            count = 0
            for n in path:
                if state[n] == 1:
                    count += 1
            if count == len(path):
                working_states.append(state)
                break
    return working_states


def get_probability(working_sates):
    probability = []
    for state in working_sates:
        state_prob = 1
        for i in range(len(state)):
            state_prob *= abs(1 - state[i] - PROBABILITY_ARRAY[i])
        probability.append(state_prob)
    return probability


def lab2():
    a = np.asarray(INPUT_ARRAY)
    G = nx.DiGraph(a)

    path_list = get_path_list(G)

    print('Кількість можливих шляхів: {:}'.format(len(path_list)))
    print('Шлях по вершинам')
    for path in path_list:
        print([n+1 for n in path])
    working_states = get_state_list(path_list)
    print('Кількість можливих робочих варіантів: {:}'.format(len(working_states)))
    probabilities = get_probability(working_states)
    print('{:<25} {:>20}'.format('Вершини', 'Ймовірність роботи'))
    print('{:}'.format(list(range(1, len(INPUT_ARRAY) + 1))))
    for state, probability in zip(working_states, probabilities):
        print('{:<25} {:>20.3}'.format(str(state), probability))
    print('\nЙмовірність безвідмовної роботи системи: {:.5}'.format(sum(probabilities)))


if __name__ == '__main__':
    if values_check():
        lab2()
