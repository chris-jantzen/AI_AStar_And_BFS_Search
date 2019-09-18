class State:
    def __init__(self, parent_state, stateid, parent_stateid):
        self.parent_state = parent_state
        self.stateid = stateid
        self.parent_stateid = parent_stateid

    def printState(self):
        nl = 1
        for i in range(len(self.parent_state)):
            if nl == 4:
                if self.parent_state[i] is 0:
                    print(' ')
                else:
                    print(self.parent_state[i])
                nl = 1
            elif self.parent_state[i] is 0:
                print('here')
            else:
                print(self.parent_state[i], end=' ')
                nl += 1


# node = State([15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#               11, 12, 13, 14, 0, 16, 17, 18, 19])
# node.printState()
