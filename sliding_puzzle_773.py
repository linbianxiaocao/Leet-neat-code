# https://blog.csdn.net/fuxuemingzhu/article/details/82919580

Hard题目真的是一个比一个看起来难，但是只要有充足的经验，能看出这个是考BFS的题目，那么剩下的时间就是套用模板了吧。。

每次移动都相当于得到了一个新的状态，同时记录得到这个状态需要的步数，并把这个状态保存到已经出现过的set里。所以，本题的难点在于使用如果把二维数组和字符串进行转化的问题，代码写的很清楚了，就不详细说了。

需要注意的是，通过二维坐标得到字符串索引的方式是x * cols + y，我觉得应该是常识，可是我第一次没想出来。

Ps，吐槽一句，python的字符画不支持直接指定某个位置的字符，因此这个题里面迫不得已用了几次string和list互转的过程。。

最坏情况下的时间复杂度是O((MN)!)，空间复杂度是O(MN)。M,N代表行列数，这个题分别为2，3.
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82919580
版权声明：本文为博主原创文章，转载请附上博文链接！

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        goal = "123450"
        start = self.board2str(board)

        bfs = collections.deque()
        bfs.append((start, 0))
        visited = set()
        visited.add(start)

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while bfs:
            path, step = bfs.popleft()

            if path == goal:
                return step
            p = path.index("0")
            x, y = p / 3, p % 3
            path = list(path)
            for dir in dirs:
                tx, ty = x + dir[0], y + dir[1]
                if tx < 0 or tx >= 2 or ty < 0 or ty >= 3:
                    continue
                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]
                pathStr = "".join(path)
                if pathStr not in visited:
                    bfs.append((pathStr, step + 1))
                    visited.add(pathStr)
                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]
        return -1

    def board2str(self, board):
        bstr = ""
        for i in range(2):
            for j in range(3):
                bstr += str(board[i][j])
        return bstr



