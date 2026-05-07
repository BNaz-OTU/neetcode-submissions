class Node:
    def __init__(self, value=None, nxt=None):
        self.val = value
        self.nxt = nxt

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        count = 0
        copy = self.head
        while copy:
            if count == index:
                return copy.val
            count += 1
            copy = copy.nxt
        
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        copy = self.head
        node = Node(val)
        while copy.nxt:
            copy = copy.nxt
        
        copy.nxt = node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.nxt
            return True
        
        copy = self.head
        count = 0
        prev = None
        while copy:
            if count == index:
                prev.nxt = copy.nxt
                return True
            count += 1
            prev = copy
            copy = copy.nxt
        
        return False

    def getValues(self) -> List[int]:
        arr = []
        copy = self.head

        while copy:
            arr.append(copy.val)
            copy = copy.nxt
        
        return arr