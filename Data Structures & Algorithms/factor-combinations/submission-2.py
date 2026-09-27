class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        final = []

        def backtrack(factors):
            if (len(factors) > 1):
                final.append(factors.copy())
            
            last_factor = factors.pop()

            i = 2 if not factors else factors[-1]
            while i <= last_factor // i:
                if last_factor % i == 0:
                    # Add i and last_factor // i
                    factors.append(i)
                    factors.append(last_factor // i)
                    backtrack(factors)
                    factors.pop()
                    factors.pop()
                
                i += 1
            
            factors.append(last_factor)

        backtrack([n])
        return final
