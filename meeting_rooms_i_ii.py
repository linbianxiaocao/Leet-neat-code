Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

我们可以先给所有区间排个序，用起始时间的先后来排，然后我们从第二个区间开始，如果开始时间早于前一个区间的结束时间，则说明会议时间有冲突，返回false，遍历完成后没有冲突，则返回true，参见代码如下


Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

这道题有好几种解法，我们先来看使用TreeMap来做的，我们遍历时间区间，对于起始时间，映射值自增1，对于结束时间，映射值自减1，然后我们定义结果变量res，和房间数rooms，我们遍历TreeMap，时间从小到大，房间数每次加上映射值，然后更新结果res，遇到起始时间，映射是正数，则房间数会增加，如果一个时间是一个会议的结束时间，也是另一个会议的开始时间，则映射值先减后加仍为0，并不用分配新的房间，而结束时间的映射值为负数更不会增加房间数，利用这种思路我们可以写出代码如下:

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        map<int, int> m;
        for (auto a : intervals) {
            ++m[a.start];
            --m[a.end];
        }
        int rooms = 0, res = 0;
        for (auto it : m) {
            res = max(res, rooms += it.second);
        }
        return res;
    }
};

http://www.cnblogs.com/grandyang/p/5244720.html


min heap solution:
Thought process:
The idea is to first sort the array based on start time, so we can examine the meetings as they take place in order (and be greedy).
Suppose we have three meetings: [0, 30], [5, 10], and [15, 20] in sorted order. When we see the second meeting, we check if its start time is later than the first meeting's end time. It's not, so we need another room. We then compare the third meeting's start time with the minimum of first two meetings' end times. If there is a meeting that ends before the third meeting starts, then we don't need another room.
So as we iterate through the array, we need to store each meeting's end time and get the minimum quickly. Min heap is a natural choice.

https://zhuhan0.blogspot.com/2017/03/leetcode-253-meeting-rooms-ii.html
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        Arrays.sort(intervals, (a, b) -> a.start - b.start);
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        for (Interval i : intervals) {
            if (!heap.isEmpty() && i.start >= heap.peek()) {
                heap.poll();
            }
            heap.offer(i.end);
        }
        return heap.size();
    }

再来一看一种使用最小堆来解题的方法，这种方法先把所有的时间区间按照起始时间排序，然后新建一个最小堆，开始遍历时间区间，如果堆不为空，且首元素小于等于当前区间的起始时间，我们去掉堆中的首元素，把当前区间的结束时间压入堆，由于最小堆是小的在前面，那么假如首元素小于等于起始时间，说明上一个会议已经结束，可以用该会议室开始下一个会议了，所以不用分配新的会议室，遍历完成后堆中元素的个数即为需要的会议室的个数，参见代码如下；

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const Interval &a, const Interval &b){return a.start < b.start;});
        priority_queue<int, vector<int>, greater<int>> q;
        for (auto a : intervals) {
            if (!q.empty() && q.top() <= a.start) q.pop();
            q.push(a.end);
        }
        return q.size();
    }
};

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        heap = []
        for i in intervals:
            # if the new meeting happens after the earliest meeting ends,
            # replace the earliest ending meeting with the new meeting
            if heap and i.start >= heap[0]:
                heappop(heap)
                heappush(heap, i.end)
            else:
                heappush(heap, i.end)

        return len(heap)
https://nb4799.neu.edu/wordpress/?p=2205


