class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        x, y = 0, 0
        max_dist = 0
        DIRECTIONS = {
            0:    ( 0,  1),   # y increases
            90:  ( 1,  0),   # x increases
            180: ( 0, -1),   # y decreases
            270: (-1,  0),   # x decreases
        }
        angle = 0
        obstacles = set(map(tuple, obstacles))
        for i in commands:
            if (i != -1) and (i != -2):
                (dx,dy) = DIRECTIONS[angle]

                for _ in range(i):
                    next_x = x + dx 
                    next_y = y + dy 
                    if (next_x, next_y) in obstacles:
                        break  
                    x = next_x
                    y = next_y
                    max_dist = max(max_dist, x**2 + y**2)
            elif i == -2:
                angle = (angle - 90) % 360
            else:
                angle = (angle + 90) % 360
        return max_dist
