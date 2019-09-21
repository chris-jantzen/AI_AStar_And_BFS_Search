class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i.state) for i in self.queue])

    def __iter__(self):
        return PriorityQueueIterator(self)

    def isEmpty(self):
        return len(self.queue) == []

    def insert(self, data):
        self.queue.append(data)

    def pop(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                # TODO figure out how to get fn here
                if self.queue[i].gn < self.queue[min].gn:
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


# Test Code
# from state import State
# prio = PriorityQueue()
# node1 = State([5, 15, 7, 8, 9, 11, 10, 3, 12, 0,
#                2, 13, 4, 14, 1, 6, 16, 17, 18, 19], 1, 0, 2)
# node2 = State([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
#                12, 13, 14, 15, 16, 17, 18, 19], 1, 0, 3)

# prio.insert(node1)
# prio.insert(node2)

# print(prio)
# item = prio.pop()
# print(prio)

# print(item)

# for i in prio:
#     print(i)
