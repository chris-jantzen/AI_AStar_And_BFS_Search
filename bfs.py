from state import State
from priority_queue import PriorityQueue
from search import Search
from utils import swapPositions


class BFS(Search):
    def __init__(self, goal_state):
        super().__init__(goal_state)
        self.open_list = PriorityQueue()
        self.closed_list = []

    def breadthFirstSearch(self, start_state):
        found_goal_state = False
        self.id_count = 1
        self.open_list.insert(start_state)
        while not found_goal_state:
            node = self.getOpenListNode()
            if node.isGoalState(self.goal_state):
                print('goal state')
                return
            # Expands node and inserts all non-duplicates into open list
            self.expandNode(node)
            self.closed_list.append(node)

    def getOpenListNode(self):
        return self.open_list.pop()

    def expandNode(self, node):
        # TODO: Make a check for side, top, bottom cases to make sure that I don't
        # loop around the side in moves
        zero_index = node.state.index(0)
        newNodes = []
        # TODO: Abstract this into another function
        if zero_index - 4 >= 0:
            newNodes.append(
                State(
                    swapPositions(node.getState().copy(),
                                  zero_index, zero_index-4),
                    self.id_count,
                    node.stateid,
                    node.gn + 1)
            )
            self.id_count += 1
        if zero_index - 1 >= 0:
            newNodes.append(
                State(
                    swapPositions(node.getState().copy(),
                                  zero_index, zero_index-1),
                    self.id_count,
                    node.stateid,
                    node.gn + 1
                )
            )
            self.id_count += 1
        if zero_index + 1 <= len(node.getState()):
            newNodes.append(
                State(
                    swapPositions(node.getState().copy(),
                                  zero_index, zero_index+1),
                    self.id_count,
                    node.stateid,
                    node.gm + 1
                )
            )
            self.id_count += 1
        if zero_index + 4 <= len(node.getState()):
            newNodes.append(
                State(
                    swapPositions(node.getState().copy(),
                                  zero_index, zero_index+4),
                    self.id_count,
                    node.stateid,
                    node.gm + 1
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
            index += 1
        for item in to_pop:
            nodes.remove(item)
        return nodes
