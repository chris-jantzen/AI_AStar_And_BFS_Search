class Search:
    def __init__(self, goal_state):
        self.goal_state = goal_state

    def swapPositions(self, lst, pos1, pos2):
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
        return lst
