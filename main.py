from bfs import BFS
from astarsearch import AStar
from state import State
from sys import argv
from ast import literal_eval


def main(start_state, goal_state, search_type):
    breadth_first_search = BFS(goal_state)
    res = breadth_first_search.breadthFirstSearch(start_state)
    # a_star_h1 = AStar(goal_state, search_type)
    # res = a_star_h1.aStar(start_state)
    # a_star_h2 = AStar(goal_state, search_type)
    # res = a_star_h2.aStar(start_state)
    for i in res:
        print(i)


if __name__ == "__main__":
    # TODO: Read in states from command line call
    # s_type = argv[1]
    # s_list = literal_eval(argv[2])
    # g_list = literal_eval(argv[3])

    start_state_list = [
        1,
        0,
        3,
        4,
        5,
        2,
        7,
        8,
        9,
        6,
        15,
        11,
        13,
        10,
        14,
        12,
        16,
        17,
        18,
        19,
    ]
    goal_state_list = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        0,
        16,
        17,
        18,
        19,
    ]
    search_type = "bfs"
    main(
        State(start_state_list, 1, 0, 0, goal_state_list, 0, search_type),
        State(goal_state_list, 0, 0, 0, goal_state_list, 0, search_type),
        search_type,
    )

# Simple State Test Case
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 17, 16, 18, 19]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15, 17, 16, 18, 19]

# Test Case 1
# [16, 17, 5, 1, 3, 4, 2, 10, 6, 8, 13, 9, 7, 12, 0, 14, 11, 15, 18, 19]
# [16, 17, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 18, 19]

# Test Case 2
# [1, 0, 3, 4, 5, 2, 7, 8, 9, 6, 15, 11, 13, 10, 14, 12, 16, 17, 18, 19]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19]

# Test Case 3
# [2, 0, 3, 4, 1, 5, 7, 8, 9, 6, 10, 12, 13, 14, 11, 15, 16, 17, 18, 19]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 17, 16, 18, 19]
