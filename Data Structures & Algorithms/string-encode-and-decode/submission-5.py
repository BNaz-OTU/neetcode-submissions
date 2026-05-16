class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for val in strs:
            final += str(len(val)) + "#" + val
        
        return final


    def decode(self, s: str) -> List[str]:
        final = []
        idx = 0
        count = ""
        while idx < len(s):
            if (s[idx] == "#"):
                final.append(s[idx + 1: idx + int(count) + 1])
                idx += int(count) + 1
                count = ""
                continue

            count += s[idx]
            idx += 1
        
        return final
