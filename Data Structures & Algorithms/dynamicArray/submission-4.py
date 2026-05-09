class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [None] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        # print(self.arr)
        # print(self.capacity, self.length)
        end = self.arr[self.length - 1]
        self.length -= 1
        self.arr = self.arr[:self.length]
        return end



    def resize(self) -> None:
        self.capacity = self.capacity * 2
        n_arr = [None] * self.capacity

        for idx in range(len(self.arr)):
            n_arr[idx] = self.arr[idx]

        self.arr = n_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
