class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for val in strs:
            final += str(len(val)) + "#" + val
        
        return final
            

    def decode(self, s: str) -> List[str]:
        finalList = []

        idx = 0
        count = ""
        while idx < len(s):
            while s[idx] != "#":
                count += s[idx]
                idx += 1

            idx += 1
            value = s[idx: idx + int(count)]
            finalList.append(value)
            idx += int(count)
            count = ""
        
        return finalList

