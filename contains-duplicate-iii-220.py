Approach #2 (Binary Search Tree) [Accepted]
https://leetcode.com/problems/contains-duplicate-iii/solution/
Java
public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
    TreeSet<Integer> set = new TreeSet<>();
    for (int i = 0; i < nums.length; ++i) {
        // Find the successor of current element
        Integer s = set.ceiling(nums[i]);
        if (s != null && s <= nums[i] + t) return true;

        // Find the predecessor of current element
        Integer g = set.floor(nums[i]);
        if (g != null && nums[i] <= g + t) return true;

        set.add(nums[i]);
        if (set.size() > k) {
            set.remove(nums[i - k]);
        }
    }
    return false;
}


Python
# https://leetcode.com/problems/contains-duplicate-iii/discuss/824603/Python-SortedList-O(n-log-k)-solution-explained.

from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])
            pos1 = SortedList.bisect_left(SList, nums[i]-t)
            pos2 = SortedList.bisect_right(SList, nums[i]+t)
            if pos1 != len(SList) and pos1 != pos2:
                return True
            SList.add(nums[i])
        return False
        
        
        
Approach #3 (Buckets) [Accepted]
https://leetcode.com/problems/contains-duplicate-iii/solution/
# https://leetcode.com/problems/contains-duplicate-iii/discuss/61639/JavaPython-one-pass-solution-O(n)-time-O(n)-space-using-buckets

bucket -> values
 1: 4, 5, 6, 7
 0: 0, 1, 2, 3
-1: -4, -3, -2, -1

def containsNearbyAlmostDuplicate(self, nums, k, t):
# https://leetcode.com/problems/contains-duplicate-iii/discuss/61639/JavaPython-one-pass-solution-O(n)-time-O(n)-space-using-buckets
    if t < 0: return False
    n = len(nums)
    d = {}
    w = t + 1
    for i in range(n):
        m = nums[i] // w
        if m in d:
            return True
        if m-1 in d and abs(nums[i] - d[m-1]) <= t:
            return True
        if m+1 in d and abs(nums[i] - d[m+1]) <= t:
            return True
        d[m] = nums[i]
        if i >= k: del d[nums[i-k] // w]
    return False
    
    