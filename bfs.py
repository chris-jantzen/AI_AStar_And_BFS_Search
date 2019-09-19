from state import State
from priority_queue import PriorityQueue
from search import Search
from math import inf

open_list = PriorityQueue()  # List of states that have been seen but not expanded
closed_list = []  # List of states that have been expanded


class BFS(Search):
    def breadthFirstSearch(self, start_state):
        found_goal_state = False
        id_count = 1
        open_list.insert(start_state)
        while not found_goal_state:
            node = self.getOpenListNode()
            # TODO: Expand the node here
            # Then add it to the closed list
            # Implement a way to compare it to things in the closed list,
            # which will basically just be like doing the goal state check.

    def getOpenListNode(self):
        min = inf
        minState = None
        for i in open_list:
            if i.fn < min:
                min = i.fn
                minState = i
        return minState

    def checkStartStateEqualsGoal(self, start):
        if start.isGoalState(self.goal_state):
            return True
        return False
