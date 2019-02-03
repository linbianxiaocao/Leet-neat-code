http://chaoren.is-programmer.com/posts/43039.html

Word Ladder II自己写的一直超时，看了discuss里的这个解法，用defaultdict，很好很强大，佩服佩服！defaultdict和普通dict的不同就是它允许有默认值，比如d = collections.defaultdict(set), 即使没有5这个key，d[5]仍然有值，是set([])。如果用int来初始化，d[5]默认值就是0。用list来初始化，d[5]默认值就是[]。我根据自己的理解写了一下注释，再次赞Python的简洁。

# 2015-06-18  Runtime: 712 ms
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dic):
        # thanks to https://leetcode.com/discuss/24191/defaultdict-for-traceback-and-easy-writing-lines-python-code
        dic.add(end)
        level = set([start])
        # key is word, value is parent word, e.g. {'hot': set(['hit']), 'cog': set(['log', 'dog'])}
        # In each level, defaultdict(set) can remove duplicates, first we need to get parent dictionary
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    for i in xrange(len(start)):
                        childWord = word[:i] + char + word[i+1:]
                        if childWord in dic and childWord not in parents: next_level[childWord].add(word)
            level = next_level
            parents.update(next_level)

        # then according parent dictionary, build result from end word to start word
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res

jie note:
关键是用字典记录转换后单词的所有parents
同时记录把所有已经处理过的单词加入那个parents的字典，如果转换后单词曾经在parents词典中出现过，就跳过该单词
一层一层遍历（即bfs）

also some helpful note from: http://yucoding.blogspot.com/2014/01/leetcode-question-word-ladder-ii.html
