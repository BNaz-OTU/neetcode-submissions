class Node:

    def __init__(self, val, nxt=None):
        self.val, self.nxt = val, nxt

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        copy = self.head
        count = 0

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
        node = Node(val)
        if self.head is None:
            self.head = node
        
        else:
            copy = self.head
            
            while copy and copy.nxt:
                copy = copy.nxt
            
            copy.nxt = node

    def remove(self, index: int) -> bool:
        copy = self.head
        count = 0
        prev = None

        while copy:
            if count == index:
                if prev:
                    prev.nxt = copy.nxt
                
                else:
                    self.head = self.head.nxt

                return True

            count += 1
            prev = copy
            copy = copy.nxt

        return False
        

    def getValues(self) -> List[int]:
        final = []
        copy = self.head

        while copy:
            final.append(copy.val)
            copy = copy.nxt

        return final
        
