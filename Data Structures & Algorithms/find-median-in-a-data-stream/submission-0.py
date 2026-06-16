class MedianFinder:

    def __init__(self):
        self.number = 0
        self.heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        self.number += 1
        

    def findMedian(self) -> float:
        count = 0
        middle = middle = self.number // 2

        copy = self.heap.copy()

        if (self.number % 2 == 1):
            while middle > count:
                heapq.heappop(copy)
                count += 1
            
            # print(f"ODD: {copy}")
            return copy[0]

        else:
            while middle - 1 > count:
                heapq.heappop(copy)
                count += 1

            # print(f"EVEN: {copy}")
            val1 = heapq.heappop(copy)
            return (copy[0] + val1) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()