https://blog.csdn.net/fuxuemingzhu/article/details/82014687
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        res = []
        s = set(pattern)
        for word in words:
            if len(word) != len(pattern) or len(set(word)) != len(s):
                continue

            d = {}
            isWordMatching = True
            for i in range(len(word)):
                letter = word[i]
                if letter not in d:
                    d[letter] = pattern[i]
                else:
                    if d[letter] != pattern[i]:
                        isWordMatching = False
                        break

            if isWordMatching:
                res.append(word)

        return res
