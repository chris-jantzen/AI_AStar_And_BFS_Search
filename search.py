from priority_queue import PriorityQueue


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
