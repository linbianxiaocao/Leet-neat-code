trie的思路

参考：
https://blog.csdn.net/ljiabin/article/details/45846527
https://blog.csdn.net/xudli/article/details/45864915
http://www.cnblogs.com/grandyang/p/4516013.html
https://www.cnblogs.com/yrbbest/p/4979650.html

python:
http://bookshadow.com/weblog/2015/05/19/leetcode-word-search-ii/

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        w, h = len(board[0]), len(board)
        trie = Trie()
        for word in words:
            trie.insert(word)

        visited = [[False] * w for x in range(h)]
        dz = zip([1, 0, -1, 0], [0, 1, 0, -1])
        ans = []

        def dfs(word, node, x, y):
            if board[x][y] not in node.childs:
                return
            node = node.childs[board[x][y]]
            visited[x][y] = True
            for z in dz:
                nx, ny = x + z[0], y + z[1]
                if nx >= 0 and nx < h and ny >= 0 and ny < w and not visited[nx][ny]:
                    dfs(word + board[nx][ny], node, nx, ny)
            if node.isWord:
                ans.append(word)
                trie.delete(word)
            visited[x][y] = False

        for x in range(h):
            for y in range(w):
                dfs(board[x][y], trie.root, x, y)

        return sorted(ans)


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.childs:
                node.childs[letter] = TrieNode()
            node = node.childs[letter]
        node.isWord = True

    def delete(self, word):
        node = self.root
        queue = []
        for letter in word:
            queue.append((letter, node))
            if letter not in node.childs:
                return False
            node = node.childs[letter]

        if not node.isWord:
            return False
        if len(node.childs):
            node.isWord = False
        else:
            for letter, node in reversed(queue):
                del node.childs[letter]
                if len(node.childs) or node.isWord:
                    break
        return True

