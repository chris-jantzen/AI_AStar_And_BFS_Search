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
            self.expandNode(node)
            return

            # TODO:
            # Expand the node here
            # Then add it to the closed list
            # Implement a way to compare it to things in the closed list,
            # which will basically just be like doing the goal state check.

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
