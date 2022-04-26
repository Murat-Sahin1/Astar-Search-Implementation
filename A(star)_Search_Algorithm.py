map_of_romania = {'Arad': [['Zerind', 75], ['Sibiu', 140], ['Timisoara', 118]],
                  'Zerind': [['Arad', 75], ['Oradea', 71]],
                  'Oradea': [['Zerind', 71], ['Sibiu', 151]],
                  'Sibiu': [['Oradea', 151], ['Arad', 140], ['Fagaras', 99], ['Rimnicu Vilcea', 80]],
                  'Rimnicu Vilcea': [['Sibiu', 80], ['Craiova', 146], ['Pitesti', 97]],
                  'Cralova': [['Rimnicu Vilcea', 146], ['Pitesti', 138], ['Dobreta', 120]],
                  'Timisoara': [['Arad', 118], ['Lugoj', 111]],
                  'Lugoj': [['Timisoara', 111], ['Mehadia', 70]],
                  'Mehadia': [['Lugoj', 70], ['Dobreta', 75]],
                  'Dobreta': [['Mehadia', 75], ['Craiova', 120]],
                  'Fagaras': [['Sibiu', 99], ['Bucharest', 211]],
                  'Pitesti': [['Rimnicu Vilcea', 97], ['Bucharest', 101]],
                  'Bucharest': [['Giurgiu', 90], ['Pitesti', 101], ['Fagaras', 211], ['Urziceni', 85]],
                  'Giurgiu': [['Bucharest', 90]],
                  'Urziceni': [['Bucharest', 85], ['Vaslui', 142], ['Hirsova', 98]],
                  'Hirsova': [['Urziceni', 98], ['Eforle', 86]],
                  'Eforie': [['Hirsova', 86]],
                  'Vaslui': [['Urziceni', 80], ['Iasi', 92]],
                  'Iasi': [['Vaslui', 92], ['Neamt', 87]],
                  'Neamt': [['Iasi', 87]]
                  }

heuristic_straight_line_dist = {'Arad': 366,
                                'Bucharest': 0,
                                'Craiova': 160,
                                'Dobreta': 242,
                                'Eforie': 161,
                                'Fagaras': 176,
                                'Giurgiu': 77,
                                'Hirsova': 151,
                                'Iasi': 226,
                                'Lugoj': 244,
                                'Mehadia': 241,
                                'Neamt': 234,
                                'Oradea': 380,
                                'Pitesti': 10,
                                'Rimnicu Vilcea': 193,
                                'Sibiu': 253,
                                'Timisoara': 329,
                                'Urziceni': 80,
                                'Vaslui': 199,
                                'Zerind': 374
                                }


class Problem:
    def __init__(self, h, target_test):
        self.initial_location = 'Arad'
        self.target_location = 'Bucharest'
        self.h = h
        self.g = 1
        self.target_test = target_test


class Node:
    def __init__(self, parent=None, state=None):
        self.parent = parent
        self.state = state
        self.f = self.h = 0


class Agent:
    def __init__(self, _enviroment, _heuristic):
        self.enviroment = _enviroment
        self.problem = Problem(_heuristic, self.target_test)
        self.current_location = self.problem.initial_location

    def target_test(self, _state):
        current_location = _state[1]
        target_location = self.problem.target_location
        if current_location == target_location:
            return True
        else:
            return False


def main():
    # first, we have our world. Second, our agent's location.
    enviroment = [map_of_romania, None]
    agent_1 = Agent(enviroment, heuristic_straight_line_dist)


main()
# print(map_of_romania['Arad'][0][1])
