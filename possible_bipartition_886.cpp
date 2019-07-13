// same as LC 785. Is Graph Bipartite?

class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/10317141.html
	// dfs: runtime and memory usage are high
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        vector<vector<int>> g(N+1, vector<int>(N+1));
        for (auto dislike : dislikes) {
            g[dislike[0]][dislike[1]] = 1;
            g[dislike[1]][dislike[0]] = 1;
        }
        vector<int> colors(N+1);
        for (int i = 1; i <= N; ++i) {
            if (colors[i] == 0 && !dfs(g, i, 1, colors)) return false;
        }
        return true;
    }
    
    bool dfs(vector<vector<int>>& g, int cur, int color, vector<int>& colors) {        
        colors[cur] = color;        
        for (int i = 1; i < g.size(); ++i) {
            if (g[cur][i] == 1) {
                if (colors[i] == color) return false;
                if (colors[i] == 0 && !dfs(g, i, -color, colors)) return false;
            }
        }     
        return true;
    }
};


class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/10317141.html
	// bfs: faster and less memory usage than dfs
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        vector<vector<int>> g(N+1);
        for (auto dislike : dislikes) {
            g[dislike[0]].push_back(dislike[1]);
            g[dislike[1]].push_back(dislike[0]);
        }
        vector<int> colors(N+1);
        for (int i = 1; i <= N; ++i) {
            if (colors[i] != 0) continue;
            colors[i] = 1;
            queue<int> q{{i}};
            while(!q.empty()) {
                int t = q.front(); 
                q.pop();
                for (int cur : g[t]) {
                    if (colors[cur] == colors[t]) return false;
                    if (colors[cur] == 0) {                        
                        colors[cur] = -colors[t];
                        q.push(cur);
                    }
                }
            }
        }
        return true;
    }
};


class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/10317141.html
    // Union Find
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        unordered_map<int, vector<int>> g;
        for (auto dislike : dislikes) {
            g[dislike[0]].push_back(dislike[1]);
            g[dislike[1]].push_back(dislike[0]);
        }
        vector<int> root(N+1);
        for (int i = 1; i <= N; ++i) root[i] = i;
        for (int i = 1; i <= N; ++i) {
            if (!g.count(i)) continue;
            int x = find(root, i), y = find(root, g[i][0]);
            if (x == y) return false;            
            for (int j = 0; j < g[i].size(); ++j) {
                int parent = find(root, g[i][j]);
                if (parent == x) return false;
                root[parent] = y;                
            }
        }
        return true;
    }
    
    int find(vector<int>& root, int i) {
        if (root[i] == i) return i;
        int p = find(root, root[i]);
        root[i] = p;
        return p;
    }
};
