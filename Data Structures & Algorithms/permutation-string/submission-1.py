class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)

        if size > len(s2):
            return False

        hash1 = {}
        for c in s1:
            hash1[c] = hash1.get(c, 0) + 1
        
        hash2 = {}

        for i in range(size):
            c = s2[i]
            hash2[c] = hash2.get(c, 0) + 1

        for i in range(len(s2) - size):
            if hash1 == hash2:
                return True

            c = s2[i]
            hash2[c] -= 1
            if hash2[c] == 0:
                del hash2[c]
            c = s2[i + size]
            hash2[c] = hash2.get(c, 0) + 1
                

        return hash1 == hash2