import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    final = []

    while len(heap) > 0:
        val = heapq.heappop(heap)
        final.append(val)
    
    return final

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
