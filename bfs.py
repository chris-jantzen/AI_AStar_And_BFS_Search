from search import Search


class BFS(Search):
    def breadthFirstSearch(self, start_state):
        self.open_list.insert(start_state)
        while True:
            node = self.getOpenListNode()
            if node.isGoalState(self.goal_state):
                path = self.getPathTaken(node)
                for i in path:
                    print(i)
                return

            # Expands node and inserts all non-duplicates into open list
            self.expandNode(node)
            self.closed_list.append(node)
