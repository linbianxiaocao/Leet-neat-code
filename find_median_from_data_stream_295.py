# 觉得比较好的参考文献：http://www.cnblogs.com/grandyang/p/4896673.html

see my own implementation in leetcode

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
