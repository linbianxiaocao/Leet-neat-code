# 简单题，自己写出来的
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        d = {}
        for i in range(26):
            d[order[i]] = chr(97 + i)

        wordsNew = []
        for word in words:
            # transform each word
            wordNew = ""
            for c in word:
                wordNew += d[c]
            wordsNew.append(wordNew)

        return wordsNew == sorted(wordsNew)

也可参考解法
https://blog.csdn.net/fuxuemingzhu/article/details/84924672
