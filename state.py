class State:
    def __init__(self, state, stateid, parent_stateid, gn, goal_state, search_type='bfs'):
        self.state = state
        self.stateid = stateid
        self.parent_stateid = parent_stateid
        self.gn = gn
        self.hn = self.calculateHeuristic(goal_state, search_type)
        self.fn = self.hn + self.gn

    def __str__(self):
        return '{}'.format(self.state)

    def printState(self):
        nl = 1
        for i in range(len(self.state)):
            if nl == 4:
                if self.state[i] == 0:
                    print(' ')
                else:
                    print(self.state[i])
                nl = 1
            else:
                if self.state[i] == 0:
                    print(' ', end=' ')
                else:
                    print(self.state[i], end=' ')
                nl += 1

    def isGoalState(self, goal_state):
        if type(goal_state) == State:
            gs = goal_state.state
        else:
            gs = goal_state
        if self.state != gs:
            return False
        return True

    def calculateHeuristic(self, goal_state, kind='bfs'):
        heuristic = 0
        if kind == 'h1':
            for state_index in range(len(self.state)):
                if self.state[state_index] != goal_state[state_index]:
                    heuristic += 1
        elif kind == 'h2':
            heuristic = self.calculateManhanttanDistance(
                self.state, goal_state)
        return heuristic

    def calculateManhanttanDistance(self, state, goal):
        hn = 0
        for state_index, state_val in enumerate(state):
            if state_val != 0:
                goal_index = goal.index(state_val)
                hn += self.steps(state_index, goal_index)
        return hn

    def steps(self, state_location, goal_location):
        return abs(state_location // 4 - goal_location // 4) + abs(state_location % 4 - goal_location % 4)

# from priority_queue import PriorityQueue
# node = State([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#               11, 12, 13, 14, 15, 16, 17, 18, 19], 1, 0)
# node2 = State([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                11, 12, 13, 14, 15, 16, 17, 18, 19], 2, 0)

# prio = PriorityQueue()
# prio.insert(node)
# prio.insert(node2)
# for i in prio:
#     print(i.state())

# node.printState()
# if node.isGoalState([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                      11, 12, 13, 14, 15, 16, 17, 18, 19]):
#     print('goal')
# else:
#     print('not goal')
