class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)

        if size > len(s2):
            return False

        hash1 = {}
        for c in s1:
            hash1[c] = hash1.get(c, 0) + 1
        
        for i in range(len(s2) - size + 1):
            st = s2[i: i + size]

            hash2 = {}

            for c in st:
                hash2[c] = hash2.get(c, 0) + 1

            if hash1 == hash2:
                return True
                

        return False