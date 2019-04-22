https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def match(self, word1, word2):
        matches = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                matches += 1
        return matches

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """

        for i in range(10):
            cnt = collections.Counter()
            for w1 in wordlist:
                for w2 in wordlist:
                    if self.match(w1, w2) == 0:
                        cnt[w1] += 1

            guess = min(wordlist, key=lambda w: cnt[w])
            n = master.guess(guess)
            if n == 6:
                return
            wordlist = [w for w in wordlist if self.match(w,guess) == n]

