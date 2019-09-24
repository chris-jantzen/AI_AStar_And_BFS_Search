from sys import argv
from ast import literal_eval


class Search:
    def __init__(self, goal_state, search_type="bfs"):
        self.goal_state = goal_state
        self.open_list = PriorityQueue()
        self.closed_list = []
        self.id_count = 1
        self._open_list_pop_count = 0
        self._open_list_add_count = 0
        self._closed_list_add_count = 0
        self.search_type = search_type

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
        self._open_list_pop_count += 1
        return self.open_list.pop()

    def checkForDuplicates(self, nodes):
        to_pop = []
        for i in nodes:
            for k in self.closed_list:
                if i.state == k.state:
                    to_pop.append(i)
                    break
            for j in self.open_list:
                if i.state == j.state:
                    if i.priority > j.priority:
                        self.open_list.remove(j)
                    else:
                        to_pop.append(i)
                    break
        for item in to_pop:
            nodes.remove(item)
        return nodes

    def returnResults(self, path):
        return (
            "Length Of Path To Get To Goal: {}".format(len(path)),
            "Nodes Pushed To Open List: {}".format(self._open_list_add_count),
            "Nodes Pushed To Closed List: {}".format(self._closed_list_add_count),
        )

class BFS(Search):
    def breadthFirstSearch(self, start_state):
        max_open_list_pops = 20000
        self.open_list.insert(start_state)
        while True:
            if self._open_list_pop_count < max_open_list_pops:
                node = self.getOpenListNode()
            else:
                return "After {} nodes popped from the open list, no solution has been found.".format(
                    max_open_list_pops
                )
            if node.isGoalState(self.goal_state):
                path = self.getPathTaken(node)
                return self.returnResults(path)

            # Expands node and inserts all non-duplicates into open list
            self.expandNode(node)
            self.closed_list.append(node)
            self._closed_list_add_count += 1

    def expandNode(self, node):
        zero_index = node.state.index(0)
        # Indexes where a zero would be on the edge of a board and would have no tile
        # to the left or right to move into its spot
        left_no_moves = [4, 8, 12, 16]
        right_no_moves = [3, 7, 11, 15]
        newNodes = []
        # TODO: Abstract this into another function
        if zero_index - 4 >= 0:
            if node.state[zero_index - 4] >= 10:
                cost = 2
            else:
                cost = 1
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(), zero_index, zero_index - 4),
                    self.id_count,
                    node.stateid,
                    node.gn + cost,
                    self.goal_state.state,
                    node.priority + 1,
                    self.search_type,
                )
            )
            self.id_count += 1
        if zero_index not in left_no_moves and zero_index - 1 >= 0:
            if node.state[zero_index - 1] >= 10:
                cost = 2
            else:
                cost = 1
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(), zero_index, zero_index - 1),
                    self.id_count,
                    node.stateid,
                    node.gn + cost,
                    self.goal_state.state,
                    node.priority + 1,
                    self.search_type,
                )
            )
            self.id_count += 1
        if zero_index not in right_no_moves and zero_index + 1 < len(node.state):
            if node.state[zero_index + 1] >= 10:
                cost = 2
            else:
                cost = 1
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(), zero_index, zero_index + 1),
                    self.id_count,
                    node.stateid,
                    node.gn + cost,
                    self.goal_state.state,
                    node.priority + 1,
                    self.search_type,
                )
            )
            self.id_count += 1
        if zero_index + 4 < len(node.state):
            if node.state[zero_index + 4] >= 10:
                cost = 2
            else:
                cost = 1
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(), zero_index, zero_index + 4),
                    self.id_count,
                    node.stateid,
                    node.gn + cost,
                    self.goal_state.state,
                    node.priority + 1,
                    self.search_type,
                )
            )
            self.id_count += 1

        newNodes = self.checkForDuplicates(newNodes)
        for i in newNodes:
            self.open_list.insert(i)
            self._open_list_add_count += 1


class AStar(Search):
    def aStar(self, start_state):
        max_open_list_pops = 20000
        self.open_list.insert(start_state)
        while True:
            if self._open_list_pop_count < max_open_list_pops:
                node = self.getOpenListNode()
            else:
                return "After {} nodes popped from the open list, no solution has been found.".format(
                    max_open_list_pops
                )
            if node.isGoalState(self.goal_state):
                path = self.getPathTaken(node)
                return self.returnResults(path)

            self.expandNode(node)
            self.closed_list.append(node)
            self._closed_list_add_count += 1

    def expandNode(self, node):
        zero_index = node.state.index(0)
        # Indexes where a zero would be on the edge of a board and would have no tile
        # to the left or right to move into its spot
        left_no_moves = [4, 8, 12, 16]
        right_no_moves = [3, 7, 11, 15]
        newNodes = []
        # TODO: Abstract this into another function
        if zero_index - 4 >= 0:
            if node.state[zero_index - 4] >= 10:
                cost = 2
            else:
                cost = 1
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(), zero_index, zero_index - 4),
                    self.id_count,
                    node.stateid,
                    node.gn + cost,
                    self.goal_state.state,
                    search_type=self.search_type,
                )
            )
            self.id_count += 1
        if zero_index not in left_no_moves and zero_index - 1 >= 0:
            if node.state[zero_index - 1] >= 10:
                cost = 2
            else:
                cost = 1
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(), zero_index, zero_index - 1),
                    self.id_count,
                    node.stateid,
                    node.gn + cost,
                    self.goal_state.state,
                    search_type=self.search_type,
                )
            )
            self.id_count += 1
        if zero_index not in right_no_moves and zero_index + 1 < len(node.state):
            if node.state[zero_index + 1] >= 10:
                cost = 2
            else:
                cost = 1
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(), zero_index, zero_index + 1),
                    self.id_count,
                    node.stateid,
                    node.gn + cost,
                    self.goal_state.state,
                    search_type=self.search_type,
                )
            )
            self.id_count += 1
        if zero_index + 4 < len(node.state):
            if node.state[zero_index + 4] >= 10:
                cost = 2
            else:
                cost = 1
            newNodes.append(
                State(
                    self.swapPositions(node.state.copy(), zero_index, zero_index + 4),
                    self.id_count,
                    node.stateid,
                    node.gn + cost,
                    self.goal_state.state,
                    search_type=self.search_type,
                )
            )
            self.id_count += 1

        newNodes = self.checkForDuplicates(newNodes)
        for i in newNodes:
            self.open_list.insert(i)
            self._open_list_add_count += 1


class State:
    def __init__(
        self,
        state,
        stateid,
        parent_stateid,
        gn,
        goal_state,
        priority=0,
        search_type="bfs",
    ):
        self.state = state
        self.stateid = stateid
        self.parent_stateid = parent_stateid
        self.gn = gn
        self.hn = self.calculateHeuristic(goal_state, search_type)
        self.fn = self.hn + self.gn
        if search_type != "bfs":
            self.priority = self.fn
        else:
            self.priority = priority

    def __str__(self):
        return "{}".format(self.state)

    def printState(self):
        nl = 1
        for i in range(len(self.state)):
            if nl == 4:
                if self.state[i] == 0:
                    print(" ")
                else:
                    print(self.state[i])
                nl = 1
            else:
                if self.state[i] == 0:
                    print(" ", end=" ")
                else:
                    print(self.state[i], end=" ")
                nl += 1

    def isGoalState(self, goal_state):
        if type(goal_state) == State:
            gs = goal_state.state
        else:
            gs = goal_state
        if self.state != gs:
            return False
        return True

    def calculateHeuristic(self, goal_state, kind="bfs"):
        heuristic = 0
        if kind == "h1":
            for state_index in range(len(self.state)):
                if self.state[state_index] != goal_state[state_index]:
                    heuristic += 1
        elif kind == "h2":
            heuristic = self.calculateManhanttanDistance(self.state, goal_state)
        return heuristic

    def calculateManhanttanDistance(self, state, goal):
        hn = 0
        for state_index, state_val in enumerate(state):
            if state_val != 0:
                goal_index = goal.index(state_val)
                hn += self.steps(state_index, goal_index)
        return hn

    def steps(self, state_location, goal_location):
        return abs(state_location // 4 - goal_location // 4) + abs(
            state_location % 4 - goal_location % 4
        )


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return " ".join([str(i.state) for i in self.queue])

    def __iter__(self):
        return PriorityQueueIterator(self)

    def isEmpty(self):
        return len(self.queue) == []

    def insert(self, node):
        self.queue.append(node)

    def remove(self, node):
        self.queue.remove(node)

    def pop(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i].priority < self.queue[min].priority:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()


class PriorityQueueIterator:
    def __init__(self, queue):
        self._queue = queue
        self._index = 0

    def __next__(self):
        if self._index < len(self._queue.queue):
            result = self._queue.queue[self._index]
            self._index += 1
            return result
        raise StopIteration


def main(start_state, goal_state, search_type):
    if search_type == "bfs":
        breadth_first_search = BFS(goal_state)
        res = breadth_first_search.breadthFirstSearch(start_state)
    elif search_type == "h1":
        a_star_h1 = AStar(goal_state, search_type)
        res = a_star_h1.aStar(start_state)
    elif search_type == "h2":
        a_star_h2 = AStar(goal_state, search_type)
        res = a_star_h2.aStar(start_state)
    else:
        print("Usage: python3 'SearchType' '[StartState]' '[EndState]'")
        print(
            "Search type = bfs, h1, or h2 where h1 is A* with count of tiles in the wrong place, and h2 is A* with Manhattan Values"
        )        
    for i in res:
        print(i)


if __name__ == "__main__":
    s_type = argv[1]
    s_list = literal_eval(argv[2])
    g_list = literal_eval(argv[3])
    main(
        State(s_list, 1, 0, 0, g_list, search_type=s_type),
        State(g_list, 0, 0, 0, g_list, search_type=s_type),
        s_type
    )

    # Testing States
    # start_state_list = [1, 0, 3, 4, 5, 2, 7, 8, 9, 6, 15, 11, 13, 10, 14, 12, 16, 17, 18, 19]
    # goal_state_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19]
    # search_type = "bfs"
    # main(
    #     State(start_state_list, 1, 0, 0, goal_state_list, 0, search_type),
    #     State(goal_state_list, 0, 0, 0, goal_state_list, 0, search_type),
    #     search_type,
    # )

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
