from search import Search


class BFS(Search):
    def breadthFirstSearch(self, start_state):
        self.open_list.insert(start_state)
        while True:
            if self._open_list_pop_count < 10000000:
                node = self.getOpenListNode()
            else:
                print('Impossible to find goal state')
            if node.isGoalState(self.goal_state):
                path = self.getPathTaken(node)
                for i in path:
                    print(i)
                print('Nodes Pushed To Open List: {}'.format(
                    self._open_list_add_count))
                print('Nodes Pushed To Closed List: {}'.format(
                    self._closed_list_add_count))
                return

            # Expands node and inserts all non-duplicates into open list
            self.expandNode(node)
            self.closed_list.append(node)
            self._closed_list_add_count += 1
