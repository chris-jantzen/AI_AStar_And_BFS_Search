class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return " ".join([str(i.state) for i in self.queue])

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
