 6. LC489 位置地形扫地机器人 高频 7次[an]
思路：常规DFS

需要用参数追踪当前机器人朝向
每次backtracking时候别忘了掉头回正
用string记录visit过的位置
参考代码：（disscussion 里面看到的代码量少，比较好写的代码）



# # """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        self.dfs(visited, 0, 0, 0, robot)

    def dfs(self, visited, i, j, currDir, robot):
        if (i, j) in visited:
            return
        visited.add((i, j))
        robot.clean()
        for k in range(4): # 4 directions
            if robot.move():
                x = i
                y = j
                if currDir == 0: # up
                    x -= 1
                elif currDir == 1: # right
                    y += 1
                elif currDir == 2: # down
                    x += 1
                elif currDir == 3: # left
                    y -= 1
                self.dfs(visited, x, y, currDir, robot)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
            robot.turnRight()
            currDir = (currDir + 1) % 4

