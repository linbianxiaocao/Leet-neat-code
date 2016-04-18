# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 
# For example,
# Given board =
# 
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.b = board
        self.m = len(board)
        self.n = len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if self.dfsIsFound(i, j, word):
                    return True
        return False

    def dfsIsFound(self, x, y, word):
        if len(word) == 0:
            return True

        if x < 0 or y < 0 or x >= self.m or y >= self.n \
                or self.b[x][y] == '#' or self.b[x][y] != word[0]:
            return False
        
        tmp = self.b[x][y]
        self.b[x][y] = '#'

        if self.dfsIsFound(x-1, y, word[1:]) or \
                self.dfsIsFound(x, y+1, word[1:]) or \
                self.dfsIsFound(x+1, y, word[1:]) or \
                self.dfsIsFound(x, y-1, word[1:]):
            return True
        self.b[x][y] = tmp

        return False
