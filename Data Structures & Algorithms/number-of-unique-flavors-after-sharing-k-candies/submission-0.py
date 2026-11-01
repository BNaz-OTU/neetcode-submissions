class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        counts = [0] * 100001
        distinct = 0
        
        for x in candies[k:]:
            if counts[x] == 0:
                distinct += 1
            
            counts[x] += 1
        
        answer = distinct
        for right in range(k, len(candies)):
            x = candies[right - k]
            if counts[x] == 0:
                distinct += 1
            
            counts[x] += 1
            x = candies[right]
            counts[x] -= 1

            if counts[x] == 0:
                distinct -= 1
            
            answer = max(answer, distinct)
        
        return answer