class State:
    def __init__(self, state, stateid, parent_stateid, gn):
        self.state = state
        self.stateid = stateid
        self.parent_stateid = parent_stateid
        self.gn = gn
        # self.hn = self.calculateHn()
        # self.fn = gn + hn

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
        for i in range(len(self.state)):
            if self.state[i] != gs[i]:
                return False
        return True


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
