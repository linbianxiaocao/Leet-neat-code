# https://zxi.mytechroad.com/blog/simulation/leetcode-683-k-empty-slots/

三种解法，brute force很好想，用bst，用buckets有点意思

"""
Author: Huahua
Runtime: 398 ms
"""
class Solution:
    def kEmptySlots(self, flowers, k):
        n = len(flowers)
        f = [0] * (n + 1)
        i = 0

        def isValid(x, k, n, f):
            f[x] = 1
            if x + k + 1 <= n and f[x + k + 1] == 1:
                valid = True
                for i in range(k):
                    if f[x + i + 1] == 1:
                        valid = False
                        break
                if valid: return True
            if x - k - 1 > 0 and f[x - k - 1] == 1:
                for i in range(k):
                    if f[x - i - 1] == 1:
                        return False
                return True
            return False

        for x in flowers:
            i += 1
            if isValid(x, k, n, f): return i

        return -1

//buckets:
// Author: Huahua
// Runtime: 196 ms (better than 94%)
class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        int n = flowers.size();
        if (n == 0 || k >= n) return -1;
        ++k;
        int bs = (n + k - 1) / k;
        vector<int> lows(bs, INT_MAX);
        vector<int> highs(bs, INT_MIN);
        for (int i = 0; i < n; ++i) {
            int x = flowers[i];
            int p = x / k;
            if (x < lows[p]) {
                lows[p] = x;
                if (p > 0 && highs[p - 1] == x - k) return i + 1;
            }
            if (x > highs[p]) {
                highs[p] = x;
                if (p < bs - 1 && lows[p + 1] == x + k) return i + 1;
            }
        }

        return -1;
    }
};

// bst
// Author: Huahua
// Runtime: 228 ms
class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        int n = flowers.size();
        if (n == 0 || k >= n) return -1;
        set<int> xs;
        for (int i = 0; i < n; ++i) {
            int x = flowers[i];
            auto r = xs.insert(x).first;
            auto l = r;
            if (++r != xs.end() && *r == x + k + 1) return i + 1;
            if (l != xs.begin() && *(--l) == x - k - 1) return i + 1;
        }

        return -1;
    }
};
