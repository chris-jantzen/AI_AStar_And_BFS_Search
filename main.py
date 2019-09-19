from bfs import BFS
from state import State


def main(start_state, goal_state):
    breadth_first_search = BFS(goal_state)
    breadth_first_search.breadthFirstSearch(start_state)


if __name__ == "__main__":
    main(
        State([5, 15, 7, 8, 9, 11, 10, 3, 12, 0,
               2, 13, 4, 14, 1, 6, 16, 17, 18, 19], 1, 0, 0),
        State([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19], 0, 0, 0)
    )
