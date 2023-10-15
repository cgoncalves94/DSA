class MaxHeap:
    def __init__(self):
        """
        Initializes an empty max heap.
        """
        self.heap = []

    def parent(self, i):
        """
        Returns the index of the parent of the element at index i.
        """
        return (i - 1) // 2

    def left_child(self, i):
        """
        Returns the index of the left child of the element at index i.
        """
        return 2 * i + 1

    def right_child(self, i):
        """
        Returns the index of the right child of the element at index i.
        """
        return 2 * i + 2

    def swap(self, i, j):
        """
        Swaps the elements at indices i and j in the heap.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        """
        Inserts a new element into the max heap.
        """
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        """
        Moves the element at index i up the heap until it is in the correct position.
        """
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_max(self):
        """
        Removes and returns the maximum element from the max heap.
        """
        if len(self.heap) == 0:
            return None

        max_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)

        return max_element

    def heapify_down(self, i):
        """
        Moves the element at index i down the heap until it is in the correct position.
        """
        while (self.left_child(i) < len(self.heap) and self.heap[i] < self.heap[self.left_child(i)]) or (self.right_child(i) < len(self.heap) and self.heap[i] < self.heap[self.right_child(i)]):

            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)] > self.heap[self.left_child(i)]:
                self.swap(i, self.right_child(i))
                i = self.right_child(i)
            else:
                self.swap(i, self.left_child(i))
                i = self.left_child(i)


def main():
    heap = MaxHeap()

    heap.insert(5)
    heap.insert(3)
    heap.insert(17)
    heap.insert(10)
    heap.insert(84)
    heap.insert(19)

    print(heap.heap)

    print(heap.extract_max())
    print(heap.extract_max())
    
    print(heap.heap)
    
if __name__ == "__main__":  
    main()