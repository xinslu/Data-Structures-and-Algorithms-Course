class MinHeap:
    def __init__(self):
        self.heap = []

    def parentPosition(self, i):
        return (i - 1) // 2

    def leftChildPosition(self, i):
        return (2 * i + 1)

    def rightChildPosition(self, i):
        return (2 * i + 2)

    def hasParent(self, i):
        return self.parentPosition(i) < len(self.heap) and self.parentPosition(i) > 0

    def hasLeftChild(self, i):
        return self.leftChildPosition(i) < len(self.heap)

    def hasRightChild(self, i):
        return self.rightChildPosition(i) < len(self.heap)

    def insertKey(self, k):
        self.heap.append(k)
        self.heapify(len(self.heap) - 1)

    def heapify(self, i):
        while(self.hasParent(i) and self.heap[i] < self.heap[self.parentPosition(i)]):
            self.heap[i], self.heap[self.parentPosition(
                i)] = self.heap[self.parentPosition(i)], self.heap[i]
            i = self.parentPosition(i)
        if not(min(self.heap) == self.heap[0]):
            if len(self.heap) >= 3:
                minidx = min(
                    enumerate([self.heap[1], self.heap[2]]), key=lambda x: x[1])[0]
                self.heap[0], self.heap[minidx +
                                        1] = self.heap[minidx + 1], self.heap[0]
            else:
                self.heap[0], self.heap[1] = self.heap[1], self.heap[0]

    def decreaseKey(self, i, new_val):
        self.heapify(len(self.heap) - 1)
        self.heap[i] = new_val
        self.heapify(len(self.heap) - 1)

    def extractMin(self):
        return self.heap.pop(0)

    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]


class MaxHeap:
    def __init__(self):
        self.heap = []

    def parentPosition(self, i):
        return (i - 1) // 2

    def leftChildPosition(self, i):
        return (2 * i + 1)

    def rightChildPosition(self, i):
        return (2 * i + 2)

    def hasParent(self, i):
        return self.parentPosition(i) < len(self.heap) and self.parentPosition(i) > 0

    def hasLeftChild(self, i):
        return self.leftChildPosition(i) < len(self.heap)

    def hasRightChild(self, i):
        return self.rightChildPosition(i) < len(self.heap)

    def insertKey(self, k):
        self.heap.append(k)
        self.heapify(len(self.heap) - 1)

    def heapify(self, i):
        while(self.hasParent(i) and self.heap[i] > self.heap[self.parentPosition(i)]):
            self.heap[i], self.heap[self.parentPosition(
                i)] = self.heap[self.parentPosition(i)], self.heap[i]
            i = self.parentPosition(i)
        if not(max(self.heap) == self.heap[0]):
            if len(self.heap) >= 3:
                maxidx = max(
                    enumerate([self.heap[1], self.heap[2]]), key=lambda x: x[1])[0]
                self.heap[0], self.heap[maxidx +
                                        1] = self.heap[maxdx + 1], self.heap[0]
            else:
                self.heap[0], self.heap[1] = self.heap[1], self.heap[0]

    def increaseKey(self, i, new_val):
        self.heapify(len(self.heap) - 1)
        self.heap[i] = new_val
        self.heapify(len(self.heap) - 1)

    def extractMax(self):
        return self.heap.pop(0)

    def deleteKey(self, i):
        self.decreaseKey(i, float("inf"))
        self.extractMax()

    def getMax(self):
        return self.heap[0]
