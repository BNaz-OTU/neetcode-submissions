class Node:
    def __init__(self, val=None, nextval=None):
        self.val = val
        self.nextval = nextval


class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        copy = self.head
        counter = 0

        while copy:
            if counter == index:
                return copy.val

            copy = copy.nextval
            counter += 1

        return -1
        

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        

    def insertTail(self, val: int) -> None:
        copy = self.head
        node = Node(val)

        if self.head is None:
            self.head = node
        
        else:
            while copy and copy.nextval:
                copy = copy.nextval
            
            copy.nextval = node

        

    def remove(self, index: int) -> bool:
        copy = self.head
        counter = 0
        prev = None

        while copy:
            if counter == index:
                if prev:
                    prev.nextval = copy.nextval
                else:
                    self.head = self.head.nextval
                return True
            counter += 1
            prev = copy
            copy = copy.nextval

        return False
        

    def getValues(self) -> List[int]:
        copy = self.head
        final = []

        while copy:
            final.append(copy.val)
            copy = copy.nextval
        
        return final
        
