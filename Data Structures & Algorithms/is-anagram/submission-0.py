class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_a = {}
        count_b = {}

        for char in s:
            count_a[char] = count_a.get(char, 0) + 1
        for char in t:
            count_b[char] = count_b.get(char, 0) + 1

        return count_a == count_b
        