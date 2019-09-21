from priority_queue import PriorityQueue
from state import State


class Search:
    def __init__(self, goal_state):
        self.goal_state = goal_state
        self.open_list = PriorityQueue()
        self.closed_list = []
        self.id_count = 1

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

    def getOpenListNode(self):
        return self.open_list.pop()

    def checkForDuplicates(self, nodes):
        to_pop = []
        for i in nodes:
            for j in self.open_list:
                if i.state == j.state:
                    to_pop.append(i)
                    break
            for k in self.closed_list:
                if i.state == k.state:
                    to_pop.append(i)
                    break
        for item in to_pop:
            nodes.remove(item)
        return nodes

    def expandNode(self, node):
        zero_index = node.state.index(0)
        # Indexes where a zero would be on the edge of a board and would have no tile
        # to the left or right to move into its spot
        left_no_moves = [4, 8, 12, 16]
        right_no_moves = [3, 7, 11, 15]
        newNodes = []
        # TODO: Abstract this into another function
        if zero_index - 4 >= 0:
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(),
                                       zero_index, zero_index-4),
                    self.id_count,
                    node.stateid,
                    node.gn + 1)
            )
            self.id_count += 1
        if zero_index not in left_no_moves and zero_index - 1 >= 0:
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(),
                                       zero_index, zero_index-1),
                    self.id_count,
                    node.stateid,
                    node.gn + 1
                )
            )
            self.id_count += 1
        if zero_index not in right_no_moves and zero_index + 1 < len(node.state):
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(),
                                       zero_index, zero_index+1),
                    self.id_count,
                    node.stateid,
                    node.gn + 1
                )
            )
            self.id_count += 1
        if zero_index + 4 < len(node.state):
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(),
                                       zero_index, zero_index+4),
                    self.id_count,
                    node.stateid,
                    node.gn + 1
                )
            )
            self.id_count += 1

        newNodes = self.checkForDuplicates(newNodes)
        for i in newNodes:
            self.open_list.insert(i)
