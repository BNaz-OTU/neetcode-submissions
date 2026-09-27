class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # 1 2 3 4 5 6 7 8 9 0
        # 1 - - - - 6 - 8 9 0
        pot_nums = [
            ["1", "1"], ["6", "9"], ["8", "8"], ["9", "6"], ["0", "0"]
        ]

        final = []

        def backtrack(n, final_length):
            if n == 0:
                return [""]
            
            if n == 1:
                return ["0", "1", "8"]

            prev = backtrack(n - 2, final_length)
            curr = []

            for prev_num in prev:
                for pair in pot_nums:
                    if pair[0] != '0' or n != final_length:
                        curr.append(pair[0] + prev_num + pair[1])
            
            return curr

        return backtrack(n, n)