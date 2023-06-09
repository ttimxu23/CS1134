"""
tzx201_hw6_q1
"""

from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, val):
        self.data.add_last(val)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.delete_first()
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.header.next.data
    
def main():
    q = LinkedQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue()) #should be 1
    print(q.first()) #should be 2

if __name__ == "__main__":
    main()

