class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i.getState()) for i in self.queue])

    def __iter__(self):
        return PriorityQueueIterator(self)

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == []

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i].gn > self.queue[max].gn:
                    max = i
            item = self.queue[max]
            del self.queue[max]
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
# prio = PriorityQueue()
# prio.insert(1)
# prio.insert(10)
# prio.insert(5)
# prio.insert(100)
# prio.insert(15)
# prio.insert(102)
# prio.insert(3)

# print(prio)
# item = prio.delete()
# print(prio)

# print(item)

# for i in prio:
#     print(i)
