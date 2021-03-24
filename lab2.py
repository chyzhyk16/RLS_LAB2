import numpy as np
import networkx as nx
import itertools as it

INPUT_ARRAY = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], ]

PROBABILITY_ARRAY = [0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.92, 0.94]

STARTING_ELEMENT = [1]

END_ELEMENT = [7, 8]

TIME = 1000

K = 1


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


def get_probability(working_sates, prob=PROBABILITY_ARRAY):
    probability = []
    for state in working_sates:
        state_prob = 1
        for i in range(len(state)):
            state_prob *= abs(1 - state[i] - prob[i])
        probability.append(state_prob)
    return probability


def lab2():
    a = np.asarray(INPUT_ARRAY)
    G = nx.DiGraph(a)

    path_list = get_path_list(G)

    print('Кількість можливих шляхів: {:}'.format(len(path_list)))
    working_states = get_state_list(path_list)
    print('Кількість можливих робочих варіантів: {:}'.format(len(working_states)))
    probabilities = get_probability(working_states)
    print('{:<25} {:>20}'.format('Вершини', 'Ймовірність роботи'))
    print('{:}'.format(list(range(1, len(INPUT_ARRAY) + 1))))
    for state, probability in zip(working_states, probabilities):
        print('{:<25} {:>20.3}'.format(str(state), probability))
    print('\nЙмовірність безвідмовної роботи системи: {:.5}'.format(sum(probabilities)))


def get_t(p):
    return (-1 * TIME) / np.log(p)


def lab3():
    a = np.asarray(INPUT_ARRAY)
    G = nx.DiGraph(a)
    path_list = get_path_list(G)
    working_states = get_state_list(path_list)
    probabilities = get_probability(working_states)
    p_system = sum(probabilities)
    q_system = 1 - p_system
    t_system = get_t(p_system)
    pqt_system = [p_system, q_system, t_system]
    q_res_system = q_system / np.math.factorial(K + 1)
    p_res_system = 1 - q_res_system
    t_res_system = get_t(p_res_system)
    pqt_res_system = [p_res_system, q_res_system, t_res_system]
    g_pqt_res_system = [pqt_res_system[i] / pqt_system[i] for i in range(len(pqt_system))]
    print(
        'Ймовірність відмови на час {0} годин = {2:.5}\n'
        'Ймовірність безвідмовної роботи на час {0} годин = {1:.5}\n'
        'Середній наробіток до відмови системи без резервування = {3:.5}\n'.format(TIME, p_system, q_system, t_system))
    print(
        'Ймовірність відмови на час {0} годин системи з загальним ненавантаженим резервуванням з кратністю {4} = {2:.5}\n'
        'Ймовірність безвідмовної роботи на час {0} годин системи з загальним ненавантаженим резервуванням = {1:.5}\n'
        'Середній наробіток до відмови системи з загальним ненавантаженим резервуванням = {3:.5}\n'.format(
            TIME, p_res_system, q_res_system, t_res_system, K))
    print(
        'Виграш надійності протягом часу {0} годин за ймовірністю відмов = {1[1]:.5}\n'
        'Виграш надійності протягом часу {0} годин за ймовірністю безвідмовної роботи = {1[0]:.5}\n'
        'Виграш надійності за середнім часом безвідмовної роботи: = {1[2]:.5}\n'.format(
            TIME, g_pqt_res_system, K))
    q_elemets = [(1 - x) ** (K + 1) for x in PROBABILITY_ARRAY]
    p_elemets = [1 - x for x in q_elemets]
    print(
        'Ймовірність відмови та безвідмовної роботи кожного елемента системи при його навантаженому резервуванні з кратністю {}'.format(
            K))
    for i in range(len(q_elemets)):
        print('Q = {:.5} P = {:.5}'.format(q_elemets[i], p_elemets[i]))
    probabilities = get_probability(working_states, p_elemets)
    p_res_system_2 = sum(probabilities)
    q_res_system_2 = 1 - p_res_system_2
    t_res_system_2 = get_t(p_res_system_2)
    pqt_res_system_2 = [p_res_system_2, q_res_system_2, t_res_system_2]
    g_pqt_res_system_2 = [pqt_res_system_2[i] / pqt_system[i] for i in range(len(pqt_system))]
    print(
        '\nЙмовірності відмови системи в цілому = {2:.5}\n'
        'Ймовірність безвідмовної роботи системи в цілому = {1:.5}\n'
        'Середній наробіток до відмови системи в цілому = {3:.5}\n'.format(TIME, p_res_system_2, q_res_system_2, t_res_system_2))
    print(
        'Виграш надійності за ймовірністю відмов = {1[1]:.5}\n'
        'Виграш надійності за ймовірністю безвідмовної роботи = {1[0]:.5}\n'
        'Виграш надійності за середнім часом безвідмовної роботи: = {1[2]:.5}\n'.format(
            TIME, g_pqt_res_system_2, K))

if __name__ == '__main__':
    if values_check():
        lab3()
