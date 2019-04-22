# Given a set of strings which just has lower case letters and a target string, output all the strings for each the edit distance with the target no greater than k.

理解这个问题首先要理解 edit distance的状态转移方程。
这题本质是在Trie树上做动态规划，类似于每一个节点上，表示从root走到这个节点形成的前缀与字符串的每一个前缀的编辑距离，这是基本思路。
dp[i]是当前结点对应的单词到target第i位第最小花费
next与dp一个含义，相当于dp'接下来的查找如果还用dp，那么会对上一层有影响，所以需要另一个数组
a. 首先是dp和next。
我们都知道在最一般的edit distance问题里面，dp[i][j] 代表着 word1[0:i]到word2[0:j]的编辑距离，并且很容易知道这样的转移方程：
if (word1.charAt(i - 1) == word2.char(j - 1)) {
dp[i][j] = dp[i - 1][j - 1]; // 字符相同，不需要编辑
} else {
dp[i][j] = 1 + Math.min(dp[i - 1][j - 1]
, Math.min(dp[i][j - 1], dp[i - 1][j]));
// 字符不一，那么存在insertion或subsitution，
// 意味着编辑距离为之前最小可能的编辑距离+1
}
捋清了这个，再来理解dp和next就很容易：
我们注意到上面的转移方程任意时候都只需要至多前一步的信息，所以我们只需要两个数组，一个标记前一步的情形，一个标记现在的情形 i.e. 用dp[j] 标记 以前的dp[i - 1][j], 以next[j] 代表以前的dp[i][j]。 那么也必然有：
if (word1.charAt(i - 1) == word2.char(j - 1)) {
next[j] = dp[j - 1]; // 老的dp[i][j] => next[j],
//老的dp[i - 1][j - 1] => dp[j - 1]
} else {
next[j]= 1 + Math.min(dp[j - 1],
Math.min(next[j - 1], dp[j]));
// 老的dp[i][j-1] => next[j - 1],
//老的dp[i - 1][j] => dp[j]
}

直接用edit distance挨个遍历一遍也能做，但是如果word list很大，那重复计算会非常多，这时候可以用trie来优化。 下面举个例，假设字典为["cs", "ct", "cby"]，target word为"cat"，k=1。 首先建Trie:
     c
   / | \
  b  s  t
 /
y
从根节点开始搜索，遍历的单词分别为：c -> cb -> (cby) -> cs -> ct。 与普通的Edit distance动态规划算法一样，我们对每一个“路过”的单词记录一个DP table。那么所遍历的单词的DP table应该为(假设当前遍历单词，也就是下面代码中的path为”c”)：
          c a t
      [ 0 1 2 3 ] <- prev_dist
-> c  [ 1 0 1 2 ] <- cur_dist
   cb [ 2 1 1 2 ]
   cs [ 2 1 1 2 ]
   ct [ 2 1 1 1 ]
每一行的最后一位数字即为当前单词与target word的edit distance。显然，如果该值小于等于k，则加入到结果中。最终返回的结果只有一个单词，即ct。

注意，遍历到单词cb时，edit distance已经为2，且长度已经与cat相等，
(这边作者有笔误，cb->cat 距离是2，但cbt->cat距离又减回1，所以一定要加一个长度相等的判断)

也就意味着该节点的子树中所包含的单词与target word的edit distance无论如何都不可能小于等于k，因此直接从该子树返回。所以单词cby是没有被遍历到的。这也就是Trie做这题的便利之处，当字典较大时会明显提高效率。


class TrieNode {
    /* Attributes in Trie */
    public TrieNode[] children;
    public boolean hasWord;
    public String str;

    /* Initialize the children and the hasWord */
    public TrieNode() {
        children = new TrieNode[26];
        for (int i = 0; i < 26; ++i)
            children[i] = null;
        hasWord = false;
    }

    /* Adds a word into the data structure. */
    static public void addWord(TrieNode root, String word) {
        TrieNode now = root; /* Traverse pointer */

        for (int i = 0; i < word.length(); i++) { /* traverse every char */
            Character c = word.charAt(i);
            if (now.children[c - 'a'] == null) {
                now.children[c - 'a'] = new TrieNode(); /* Create new child */
            }
            now = now.children[c - 'a']; /* Or get the child */
        }
        now.str = word; /* The whole word */
        now.hasWord = true; /* Mark the word */
    }
}

    public List<String> kDistance(String[] words, String target, int k) {

        TrieNode root = new TrieNode(); /* Need a virtual root */
        for (int i = 0; i < words.length; i++)
            TrieNode.addWord(root, words[i]); /* Add words to the Trie */

        List<String> result = new ArrayList<String>();

        int n = target.length();

        /*
         * State: dp[i] means walking down the trie from the virtual root to the current node, the
         * min edit distance between the formed prefix and the target's 0 to ith characters.
         */
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; ++i)
            dp[i] = i;

        find(root, result, k, target, dp);
        return result;
    }

    public void find(TrieNode node, List<String> result, int k, String target, int[] dp) {

        int n = target.length();

        if (node.hasWord && dp[n] <= k) { /* Where the answer satisfies */
            result.add(node.str);
        }

        /* Each search we need to create a new dp */
        int[] next = new int[n + 1];
        for (int i = 0; i <= n; ++i)
            next[i] = 0;

        for (int i = 0; i < 26; ++i) /* 26 Characters */
            if (node.children[i] != null) {
                next[0] = dp[0] + 1; /* Init */
                for (int j = 1; j <= n; j++) {
                    if (target.charAt(j - 1) - 'a' == i) { /* Matches */
                        next[j] = Math.min(dp[j - 1], Math.min(next[j - 1] + 1,
                                dp[j] + 1)); /* Check two j - 1 check one dp j */
                    } else { /* Does not match */
                        next[j] = Math.min(dp[j - 1] + 1, Math.min(next[j - 1] + 1, dp[j] + 1));
                        /* Check two j - 1 check one dp j */
                    }
                }
                find(node.children[i], result, k, target, next);
            }
    }

// 以上答案没有用到剪枝，看我leetcode里面代码实现 (发现以上解法没有剪枝是有道理的，不好直接减）
import sys

class TrieNode(object):
    def __init__(self):
        self.childs = {}
        self.isWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node.childs:
                node.childs[letter] = TrieNode()
            node = node.childs[letter]
        node.isWord = True

class Solution(object):
    def findWords(self, target, words, K):
        self.K = K
        self.trie = Trie()
        for word in words:
            self.trie.addWord(word)

        self.res = []
        dp = [i for i in range(len(target)+1)]
        self.dfs(self.trie.root, "", target, dp)
        return self.res

    def dfs(self, node, path, target, dp):
        if node.isWord and dp[-1] <= self.K:
            self.res.append(path)

        for letter, next in node.childs.items():
            np = [0 for _ in range(len(target) + 1)]
            np[0] = len(path)+1
            for j in range(1, len(target) + 1):
                u = 0 if letter == target[j-1] else 1
                np[j] = min(np[j-1]+1, dp[j]+1, dp[j-1] + u)
            # print(path+letter, ", ", dp, ", ", np)

            self.dfs(next, path+letter, target, np)

words = ["abc", "abd", "abcd", "adc"]
target = "ac"
k = 1
s = Solution()
res = s.findWords(target, words, k)
print(res)
