# https://www.hrwhisper.me/leetcode-find-median-from-data-stream/

import heapq
class MedianFinder:

    def __init__(self):
        self.left = []  # max heap
        self.right = [] # min heap        

    def addNum(self, num: int) -> None:
        if not self.left or num < -self.left[0]:
            heapq.heappush(self.left, -num)
            if len(self.left) >= len(self.right) + 2:
                temp = heapq.heappop(self.left)
                heapq.heappush(self.right, -temp)
        else:
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left):
                temp = heapq.heappop(self.right)
                heapq.heappush(self.left, -temp)

    def findMedian(self) -> float:
        ll = len(self.left)
        lr = len(self.right)
        if (ll + lr) % 2 == 1:
            return -self.left[0]   
        else:
            return (-self.left[0] + self.right[0]) / 2     


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# 觉得比较好的参考文献：http://www.cnblogs.com/grandyang/p/4896673.html

#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

class MedianFinder {
public:
    // from grandyang
    // void addNum(int num) {
    //     small.push(num);
    //     long st = small.top();
    //     small.pop();
    //     large.push(-st);
    //     if (small.size() < large.size()) {
    //         small.push(-large.top());
    //         large.pop();
    //     }
    // }

    // a faster solution: https://www.hrwhisper.me/leetcode-find-median-from-data-stream/
    void addNum(int num) {
        if (!large.empty() && num > -large.top())
            large.push(-num);
        else
            small.push(num);

        if (small.size()-large.size() == 2) {
            large.push(-small.top());
            small.pop();
        }
        else if (small.size()-large.size() == -2) {
            small.push(-large.top());
            large.pop();
        }
    }

    double findMedian() {
        if (small.size() > large.size()) return small.top();
        else if (small.size() < large.size()) return -large.top();
        return (small.top() - large.top()) / 2.0;
    }

private:
    priority_queue<int> small, large;

};
