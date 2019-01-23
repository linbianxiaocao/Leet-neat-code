easy problem

class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        if (s.size() < t.size()) swap(s, t);
        int m = s.size(), n = t.size(), diff = m - n;
        if (diff >= 2) return false;
        else if (diff == 1) {
            for (int i = 0; i < n; ++i) {
                if (s[i] != t[i]) {
                    return s.substr(i + 1) == t.substr(i);
                }
            }
            return true;
        } else {
            int cnt = 0;
            for (int i = 0; i < m; ++i) {
                if (s[i] != t[i]) ++cnt;
            }
            return cnt == 1;
        }
    }
};

我们实际上可以让代码写的更加简洁，只需要对比两个字符串对应位置上的字符，如果遇到不同的时候，这时我们看两个字符串的长度关系，如果相等，那么我们比较当前位置后的字串是否相同，如果s的长度大，那么我们比较s的下一个位置开始的子串，和t的当前位置开始的子串是否相同，反之如果t的长度大，那么我们比较t的下一个位置开始的子串，和s的当前位置开始的子串是否相同。如果循环结束，都没有找到不同的字符，那么此时我们看两个字符串的长度是否相差1，参见代码如下：

class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        for (int i = 0; i < min(s.size(), t.size()); ++i) {
            if (s[i] != t[i]) {
                if (s.size() == t.size()) return s.substr(i + 1) == t.substr(i + 1);
                else if (s.size() < t.size()) return s.substr(i) == t.substr(i + 1);
                else return s.substr(i + 1) == t.substr(i);
            }
        }
        return abs((int)s.size() - (int)t.size()) == 1;
    }
};
