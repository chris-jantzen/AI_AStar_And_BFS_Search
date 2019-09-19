from state import State
from priority_queue import PriorityQueue
from search import Search
from math import inf


class BFS(Search):
    def __init__(self, goal_state):
        super().__init__(goal_state)
        self.open_list = PriorityQueue()
        self.closed_list = []

    def breadthFirstSearch(self, start_state):
        found_goal_state = False
        id_count = 1
        self.open_list.insert(start_state)
        while not found_goal_state:
            node = self.getOpenListNode()
            if node.isGoalState(self.goal_state):
                print('goal state')
                return

            # TODO:
            # Expand the node here
            # Then add it to the closed list
            # Implement a way to compare it to things in the closed list,
            # which will basically just be like doing the goal state check.

    def getOpenListNode(self):
        return self.open_list.pop()
