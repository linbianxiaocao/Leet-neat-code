# http://www.cnblogs.com/grandyang/p/9362777.html

反过来算

1. dfs
首先我们来想，我们肯定要统计出当前没有掉落的砖头数量，当去掉某个砖头后，我们可以统计当前还连着的砖头数量，二者做差值就是掉落的砖头数量。那么如何来统计不会掉落的砖头数量呢，由于顶层的砖头时不会掉落的，那么跟顶层相连的所有砖头肯定也不会掉落，我们就可以使用DFS来遍历，我们可以把不会掉落的砖头位置存入一个HashSet中，这样通过比较不同状态下HashSet中元素的个数，我们就知道掉落了多少砖头。然后我们再来想一个问题，在没有去除任何砖头的时候，我们DFS查找会遍历所有的砖头，当某个砖头去除后，可能没有连带其他的砖头，那么如果我们再来遍历一遍所有相连的砖头，相当于又把整个数组搜索了一遍，这样并不是很高效。我们可以试着换一个思路，如果我们先把要去掉的所有砖头都先去掉，这样我们遍历所有相连的砖头就是最终还剩下的砖头，然后我们从最后一个砖头开始往回加，每加一个砖头，我们就以这个砖头为起点，DFS遍历其周围相连的砖头，加入HashSet中，那么只会遍历那些会掉的砖头，那么增加的这些砖头就是会掉的砖头数量了，然后再不停的在增加前面的砖头，直到把hits中所有的砖头都添加回来了，那么我们也就计算出了每次会掉的砖头的个数。

好，我们使用一个HashSet来保存不会掉落的砖头，然后先遍历hits数组，把要掉落的砖头位置的值都减去一个1，这里有个需要注意的地方，hits里的掉落位置实际上在grid中不一定有砖头，就是说可能是本身为0的位置，那么我们减1后，数组中也可能会有-1，没有太大的影响，不过需要注意一下，这里不能使用 if (grid[i][j])
来直接判断其是否为1，因为非0值-1也会返回true。
然后我们对第一行的砖头都调用递归函数，因为顶端的砖头不会掉落，跟顶端的砖头相连的砖头也不会掉落，所以要遍历所有相连的砖头，将位置都存入noDrop。然后就是从最后一个位置往前加砖头，先记录noDrop当前的元素个数，然后grid中对应的值自增1，之后增加后的值为1了，才说明这块之前是有砖头的，然后我们看其上下左右位置，若有砖头is in noDrop set，则对当前位置调用递归，
Attention:还有一种情况是当前是顶层的话，还是要调用递归。递归调用完成后二者的差值再减去1就是掉落的砖头数，减1的原因是去掉的砖头不算掉落的砖头数中，参见代码如:
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * len(hits)
        m, n = len(grid), len(grid[0])
        noDrop = set()
        for i in range(len(hits)):
            hit = hits[i]
            grid[hit[0]][hit[1]] -= 1

        # scan top
        for j in range(n):
            if grid[0][j] == 1:
                self.dfs(grid, 0, j, noDrop)

        for i in range(len(hits))[::-1]:
            oldSize = len(noDrop)
            x, y = hits[i]
            grid[x][y] += 1
            if grid[x][y] != 1: continue

            # 关键代码，检查邻居是否连着noDrop里面的点
            if (y+1<n and (x, y+1) in noDrop) or\
               (x+1<m and (x+1, y) in noDrop) or\
               (y-1>=0 and (x, y-1) in noDrop) or\
               (x-1>=0 and (x-1, y) in noDrop) or\
               x == 0: # 特殊处理顶端砖块
                self.dfs(grid, x, y, noDrop)
                res[i] = len(noDrop)-oldSize-1

        return res

    def dfs(self, grid, i, j, noDrop):
        m, n = len(grid), len(grid[0])
        if i<0 or i>=m or j<0 or j>=n or grid[i][j] != 1:
            return
        if (i, j) in noDrop:
            return

        noDrop.add((i, j))
        self.dfs(grid, i, j+1, noDrop)
        self.dfs(grid, i+1, j, noDrop)
        self.dfs(grid, i, j-1, noDrop)
        self.dfs(grid, i-1, j, noDrop)



