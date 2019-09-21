from search import Search


class AStar(Search):
    def aStar(self, start_state):
        self.open_list.insert(start_state)
        while True:
            if self._open_list_pop_count < 1000000:
                # Verify this is okay to use for both.
                # Should be since it will be using f(n)
                node = self.getOpenListNode()
            else:
                print('Impossible to find goal state')
                return
            if node.isGoalState(self.goal_state):
                path = self.getPathTaken(node)
                return self.returnResults(path)

            self.expandNode(node)
            self.closed_list.append(node)
            self._closed_list_add_count += 1
