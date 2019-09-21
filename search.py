class Search:
    def __init__(self, goal_state):
        self.goal_state = goal_state

    def swapPositions(self, lst, pos1, pos2):
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
        return lst

    def getPathTaken(self, goal):
        path = [goal]
        node = goal
        found_original = False
        while not found_original:
            for closed in self.closed_list:
                if node.parent_stateid == closed.stateid:
                    node = closed
                    path.append(node)
                    if node.stateid == 1:
                        found_original = True
                    break
        path.reverse()
        return path
