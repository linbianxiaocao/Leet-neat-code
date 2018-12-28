class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])
        sprialList = []

        k = 0
        while m > 0 and n > 0:
            self.printSprial(k, matrix, m, n, sprialList)
            m -= 2
            n -= 2
            k += 1
        return sprialList

    def printSprial(self, k, matrix, m, n, sprialList):

        # first row, left to right
        for j in range(0, n):
            sprialList.append(matrix[k][j+k])

        # last column, up to bottom
        for i in range(1, m):
            sprialList.append(matrix[i+k][n-1+k])

        # last row, right to left
        if m != 1:
            for i in range(n-2, -1, -1):
                sprialList.append(matrix[k+m-1][i+k])

        # first column bottom to up
        if n != 1:
            for j in range(m-2, 0, -1):
                sprialList.append(matrix[j+k][k])

        return
