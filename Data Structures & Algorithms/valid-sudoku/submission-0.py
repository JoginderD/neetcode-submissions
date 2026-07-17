class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hashSet = set()
            for n in board[i]:
                if n == ".":
                    continue
                if n in hashSet:
                    return False
                else:
                    hashSet.add(n)

        for j in range(9):
            hashSet = set()
            for k in range(9):
                n = board[k][j]

                if n == ".":
                    continue
                if n in hashSet:
                    return False
                else:
                    hashSet.add(n)

        for l in range(0, 9, 3):
            for p in range(0, 9, 3):
                hashSet = set()

                for o in range(l, l + 3):
                    for q in range(p, p + 3):
                        n = board[o][q]

                        if n == ".":
                            continue

                        if n in hashSet:
                            return False
                        else:
                            hashSet.add(n)


        return True