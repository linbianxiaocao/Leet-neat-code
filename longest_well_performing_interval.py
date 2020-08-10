
Not that easy, tricky but clean
https://leetcode.com/problems/longest-well-performing-interval/discuss/334565/javacpython-on-solution-life-needs-996-and-669
https://www.youtube.com/watch?v=H76XMJmBfP0

def longestWPI(self, hours):
    res = score = 0
    seen = {}
    for i, h in enumerate(hours):
        score = score+1 if h > 8 else score-1
        if score > 0:
            res = i + 1
        if score not in seen:
            seen[score] = i
        if score-1 in seen:
            res = max(res, i - seen[score-1]
    return res