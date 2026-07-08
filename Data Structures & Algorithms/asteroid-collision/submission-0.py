class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for num in asteroids:
            s.append(num)
            if len(s) <= 1:
                continue
            elif not((s[-1] > 0 and s[-2] > 0) or (s[-1] < 0 and s[-2] < 0)):
                while len(s) >= 2 and s[-2] > 0 and s[-1] < 0:
                    if abs(s[-1]) > abs(s[-2]):
                        temp = s[-1]
                        s.pop()
                        s.pop()
                        s.append(temp)
                    elif abs(s[-1]) < abs(s[-2]):
                        s.pop()
                    elif abs(s[-1]) == abs(s[-2]):
                        s.pop()
                        s.pop()
                    else:
                        break
            
        return s
                    