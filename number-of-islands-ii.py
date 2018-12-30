# http://www.cnblogs.com/grandyang/p/5190419.html

这道题是之前那道Number of Islands的拓展，难度增加了不少，因为这次是一个点一个点的增加，每增加一个点，都要统一一下现在总共的岛屿个数，最开始初始化时没有陆地，如下：

0 0 0
0 0 0
0 0 0

假如我们在(0, 0)的位置增加一个陆地，那么此时岛屿数量为1：

1 0 0
0 0 0
0 0 0

假如我们再在(0, 2)的位置增加一个陆地，那么此时岛屿数量为2：

1 0 1
0 0 0
0 0 0

假如我们再在(0, 1)的位置增加一个陆地，那么此时岛屿数量却又变为1：

1 1 1
0 0 0
0 0 0

假如我们再在(1, 1)的位置增加一个陆地，那么此时岛屿数量仍为1：

1 1 1
0 1 0
0 0 0

那么我们为了解决这种陆地之间会合并的情况，最好能够将每个陆地都标记出其属于哪个岛屿，这样就会方便我们统计岛屿个数。这种群组类问题，很适合使用联合查找 Union Find 来做，又叫并查集 Disjoint Set，LeetCode中使用这种解法的题目还不少呢，比如Friend Circles，Graph Valid Tree，Redundant Connection II 等等。一般来说，UF算法的思路是每个个体先初始化为不同的群组，然后遍历有关联的两个个体，如果发现其getRoot函数的返回值不同，则手动将二者加入一个群组，然后总群组数自减1。这里就要分别说一下root数组，和getRoot函数。两个同群组的个体，通过getRoot函数一定会返回相同的值，但是其在root 数组中的值不一定相同，我们可以类比成getRoot函数返回的是祖先，如果两个人的祖先相同，那么其是属于一个家族的（这里不是指人类共同的祖先哈）。root可以用数组或者HashMap来表示，如果个体是数字的话，那么数组就OK，如果个体是字符串的话，可能就需要用HashMap了。root数组的初始化可以有两种，可以均初始化为-1，或者都初始化为不同的数字，博主一般喜欢初始化为不同的数字。getRoot函数的写法也可用递归或者迭代的方式，可参见博主之前的帖子Redundant Connection II中的讨论部分。这么一说感觉UF算法的东西还蛮多的，啥时候博主写个UF总结贴吧。

那么具体来看这道题吧，此题跟经典的UF使用场景有一点点的区别，因为一般的场景中两个个体之间只有两种关系，属于一个群组或者不属于同一个群组，而这道题里面由于water的存在，就多了一种情况，我们只需要事先检测一下当前位置是不是岛屿就行了，总之问题不大。一般来说我们的root数组都是使用一维数组，方便一些，那么这里就可以将二维数组encode为一维的，于是我们需要一个长度为m*n的一维数组来标记各个位置属于哪个岛屿，我们假设每个位置都是一个单独岛屿，岛屿编号可以用其坐标位置表示，但是我们初始化时将其都赋为-1，这样方便我们知道哪些位置尚未变成岛屿。然后我们开始遍历陆地数组，将其岛屿编号设置为其坐标位置，然后岛屿计数加1，我们此时开始遍历其上下左右的位置，遇到越界或者岛屿标号为-1的情况直接跳过，现在知道我们初始化为-1的好处了吧，遇到是water的地方直接跳过。否则我们用getRoot来查找邻居位置的岛屿编号，同时也用getRoot来查找当前点的编号，这一步就是经典的UF算法的操作了，因为当前这两个land是相邻的，它们是属于一个岛屿，所以其getRoot函数的返回值suppose应该是相等的，但是如果返回值不同，说明我们需要合并岛屿，将两个返回值建立关联，并将岛屿计数cnt减1。当我们遍历完当前点的所有邻居时，该合并的都合并完了，将此时的岛屿计数cnt存入结果中，参见代码如下：

# note: understand the findRoot function, basically, it's index mapping, e.g., 3 -> 3, 2 -> 4 -> 3

class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<pair<int, int>>& positions) {
        vector<int> res;
        int cnt = 0;
        vector<int> roots(m * n, -1);
        vector<vector<int>> dirs{{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
        for (auto a : positions) {
            int id = n * a.first + a.second;
            if (roots[id] == -1) {
                roots[id] = id;
                ++cnt;
            }
            for (auto dir : dirs) {
                int x = a.first + dir[0], y = a.second + dir[1], cur_id = n * x + y;
                if (x < 0 || x >= m || y < 0 || y >= n || roots[cur_id] == -1) continue;
                int p = findRoot(roots, cur_id), q = findRoot(roots, id);
                if (p != q) {
                    roots[p] = q;
                    --cnt;
                }
            }
            res.push_back(cnt);
        }
        return res;
    }
    int findRoot(vector<int>& roots, int id) {
        return (id == roots[id]) ? id : findRoot(roots, roots[id]);
    }
};

