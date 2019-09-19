from state import State
from priority_queue import PriorityQueue
from search import Search

open_list = PriorityQueue()  # List of states that have been seen but not expanded
closed_list = []  # List of states that have been expanded


class BFS(Search):
    def breadthFirstSearch(self, start_state):
        found_goal_state = False
        id_count = 1
        if self.checkStartStateEqualsGoal(start_state):
            print('Start state was goal state')
            return start_state
        while not found_goal_state:
            self.getOpenListNode()
            found_goal_state = True

    def getOpenListNode(self):
        pass

    def checkStartStateEqualsGoal(self, start):
        if start.isGoalState(self.goal_state):
            return True
        return False
