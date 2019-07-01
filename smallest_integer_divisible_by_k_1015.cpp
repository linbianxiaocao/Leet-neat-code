class Solution {
public:
    // http://www.noteanddata.com/leetcode-1022-Smallest-Integer-Divisible-by-K-google-interview-problem-java-solution-note.html
    // 可证明: if t % K = r, (t*10+1) % K = (r*10+1) % K
    // https://blog.csdn.net/fuxuemingzhu/article/details/88778532
    int smallestRepunitDivByK(int K) {
        for (int r = 0, N = 1; N <= K; ++N) {
            r = (r * 10 + 1) % K;
            if (r == 0) return N;
        }
        return -1;
    }
};
