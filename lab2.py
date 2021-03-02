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
    probability = 0
    for state in working_sates:
        state_prob = 1
        for i in range(len(state)):
            state_prob *= abs(1 - state[i] - PROBABILITY_ARRAY[i])
        probability += state_prob
    return probability
        
        
def lab2():
    a = np.asarray(INPUT_ARRAY)
    G = nx.DiGraph(a)

    path_list = get_path_list(G)

    print(len(path_list))
    print(path_list)
    working_states = get_state_list(path_list)
    print(len(working_states))
    for state in working_states[::-1]:
    	print(state)
    
    print(get_probability(working_states))
if __name__ == '__main__':
    lab2()
