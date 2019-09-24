from search import Search
from state import State


class BFS(Search):
    def breadthFirstSearch(self, start_state):
        self.open_list.insert(start_state)
        while True:
            if self._open_list_pop_count < 20000:
                node = self.getOpenListNode()
            else:
                return "After {} nodes popped from the open list, no solution has been found.".format(
                    20000
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
