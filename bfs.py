from state import State
from priority_queue import PriorityQueue
from search import Search


class BFS(Search):
    def __init__(self, goal_state):
        super().__init__(goal_state)
        self.open_list = PriorityQueue()
        self.closed_list = []

    def breadthFirstSearch(self, start_state):
        # found_goal_state = False
        self.id_count = 1
        self.open_list.insert(start_state)
        while True:
            node = self.getOpenListNode()
            if node.isGoalState(self.goal_state):
                print('goal state')
                return
            else:
                print('not goal state')
            # Expands node and inserts all non-duplicates into open list
            self.expandNode(node)
            self.closed_list.append(node)

    def getOpenListNode(self):
        return self.open_list.pop()

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
                    self.swapPositions(node.getState().copy(),
                                       zero_index, zero_index-4),
                    self.id_count,
                    node.stateid,
                    node.gn + 1)
            )
            self.id_count += 1
        if zero_index not in left_no_moves and zero_index - 1 >= 0:
            newNodes.append(
                State(
                    self.swapPositions(node.getState().copy(),
                                       zero_index, zero_index-1),
                    self.id_count,
                    node.stateid,
                    node.gn + 1
                )
            )
            self.id_count += 1
        if zero_index not in right_no_moves and zero_index + 1 <= len(node.getState()):
            newNodes.append(
                State(
                    self.swapPositions(node.getState().copy(),
                                       zero_index, zero_index+1),
                    self.id_count,
                    node.stateid,
                    node.gn + 1
                )
            )
            self.id_count += 1
        if zero_index + 4 <= len(node.getState()):
            newNodes.append(
                State(
                    self.swapPositions(node.getState().copy(),
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

    def checkForDuplicates(self, nodes):
        to_pop = []
        for i in nodes:
            for j in self.open_list:
                if i.getState() == j.getState():
                    to_pop.append(i)
                    break
            for k in self.closed_list:
                if i.getState() == k.getState():
                    to_pop.append(i)
                    break
        for item in to_pop:
            nodes.remove(item)
        return nodes
