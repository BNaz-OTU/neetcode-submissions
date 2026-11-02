# reader.get(index) is provided by the judge and returns 2147483647 outside the hidden array.
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low, high = 0, 1
        while reader.get(high) < target:
            high *= 2

        while low <= high:
            mid = (low + high) // 2
            value = reader.get(mid)

            if value == target:
                return mid
            
            if value < target:
                low = mid + 1
            
            else:
                high = mid - 1
                
        return -1
