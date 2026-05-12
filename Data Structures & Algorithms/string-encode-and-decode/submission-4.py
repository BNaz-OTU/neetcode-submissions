class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for val in strs:
            encoded += (str(len(val)) + "#" + val)
        
        return encoded
            

    def decode(self, s: str) -> List[str]:
        idx = 0
        final = []
        while idx < len(s):
            count = ""
            while idx < len(s) and s[idx] != "#":
                count += s[idx]
                idx += 1
            
            idx += 1
            num_chars = int(count)
            final.append(s[idx : idx + num_chars])
            idx += num_chars
        
        return final