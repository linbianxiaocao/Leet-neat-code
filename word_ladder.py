import sys
import collections


class Solution(object):
    def ladderLength1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self.word_chain = [beginWord, ]
        self.visited = {}
        self.shortest = sys.maxsize
        self.dfs(beginWord, endWord, wordList)
        if self.shortest < sys.maxsize:
            return self.shortest
        else:
            return 0

    # tips: 1. use BFS rather than DFS; 2. change each character of word and
    # check if changed one is in the list(dict), rather than go through each
    # word in the list to compute the distance
    # http://chaoren.is-programmer.com/posts/43039.html
    def ladderLength2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # self.word_dict = {}
        return self.bfs(beginWord, endWord, wordList)
              

#     def bfs(self, beginWord, endWord, wordList):
#         queue = collections.deque([(beginWord, 1)])
#         while queue:
#             curr_word, curr_len = queue.popleft()
#             if curr_word == endWord:
#                 return curr_len
# 
#             for word in wordList:
#                 if word not in self.word_dict\
#                    and self.diff(word, curr_word) == 1:
#                     queue.append((word, curr_len+1))
#                     self.word_dict[word] = 1
# 
#         return 0

    def bfs(self, beginWord, endWord, wordList):
        word_dict = {}
        for word in wordList:
            word_dict[word] = 0
        wlen = len(beginWord)
        queue = collections.deque([(beginWord, 1)])

        while queue:
            curr_word, curr_len = queue.popleft()
            if curr_word == endWord:
                return curr_len

            for i in range(wlen):
                part1 = curr_word[:i]
                part2 = curr_word[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if curr_word[i] != j:
                        next_word = part1 + j + part2
                        if next_word in word_dict\
                           and word_dict[next_word] == 0:
                            queue.append((next_word, curr_len+1))
                            word_dict[next_word] = 1

        return 0

    def diff(self, word1, word2):
        d = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                d += 1
                if d > 1:
                    return -1
        return 1


#     def dfs(self, beginWord, endWord, wordList):
#         if beginWord == endWord:
#             #print(self.word_chain)
#             return True
# 
#         self.visited[beginWord] = True
# 
#         for word in wordList:
#             if self.visited.get(word, False) == False\
#                and self.diff(beginWord, word) == 1:
#                 self.word_chain.append(word)
#                 if self.dfs(word, endWord, wordList):
#                     return True
#                 self.word_chain = self.word_chain[:-1]
# 
#         self.visited[beginWord] = False
# 
#         return False


#     def dfs(self, beginWord, endWord, wordList):
#         if beginWord == endWord:
#             self.shortest = min(self.shortest, len(self.word_chain))
# 
#         self.visited[beginWord] = True
# 
#         for word in wordList:
#             if self.visited.get(word, False) == False\
#                and self.diff(beginWord, word) == 1:
#                 self.word_chain.append(word)
#                 self.dfs(word, endWord, wordList)
#                 self.word_chain = self.word_chain[:-1]
# 
#         self.visited[beginWord] = False

cs = Solution()
rlen = cs.ladderLength("hit", "cog",
                       ["hot", "dot", "dog", "lot", "log", "cog"])
print(rlen)
