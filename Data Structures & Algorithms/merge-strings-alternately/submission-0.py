class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = []
        l1, l2 = len(word1), len(word2)

        while i < l1 and i < l2:
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        res.append(word1[i:])
        res.append(word2[i:])

        return "".join(res)