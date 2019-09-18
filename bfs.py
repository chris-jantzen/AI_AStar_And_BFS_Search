from state import State
from priority_queue import PriorityQueue

open_list = PriorityQueue()  # List of states that have been seen but not expanded
closed_list = []  # List of states that have been expanded


def bfs(start_state, goal_state):
    open_list.insert(start_state)
    open_list.insert(goal_state)
    for i in open_list:
        print(i)
