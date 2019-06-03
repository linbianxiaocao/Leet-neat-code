"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
import random


class Solution(object):
    # quick select algorithm (based on idea of quick sort, ref: 算法导论
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        q = self.randomPartition(nums)
        ck = n-q-1
        if ck >= k:
            return self.findKthLargest(nums[q+1:], k)
        elif ck < k:
            return self.findKthLargest(nums[0:q+1], k-ck)

    def randomPartition(self, nums):
        """
        modify nums and return q such that nums[0:q+1] <= pivot
        and nums[q+1:] >= pivot
        """
        if len(nums) == 1:
            return 0
        ridx = random.randint(0, len(nums)-1)
        # ridx = 0
        pivot = nums[ridx]
        nums[ridx] = nums[0]
        nums[0] = pivot

        i = 0
        j = len(nums)-1
        while True:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
            else:
                # print(nums)
                return j

s = Solution()
print(s.randomPartition([7, 6, 5, 4, 3, 2, 1]))



----------------cpp----------------
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 1) return nums[0];
        int q = randomPartition(nums);
        int ck = n-q-1;
        if (ck >= k) {
            vector<int> na(nums.begin()+q+1, nums.end());
            return findKthLargest(na, k);
        }
        else {
            vector<int> na(nums.begin(), nums.begin()+q+1);
            return findKthLargest(na, k-ck);
        }
    }

    int randomPartition(vector<int>& nums) {
        // modify nums and return q such that nums[0:q+1] <= pivot and
        // nums[q+1:] >= pivot
        int n = nums.size();
        if (n == 1) return 0;
        int ridx = rand() % n;
        int pivot = nums[ridx];
        swap(nums[0], nums[ridx]);

        int i = 0, j = n-1;
        while (true) {
            while (nums[i] < pivot) ++i;
            while (nums[j] > pivot) --j;
            if (i < j) {
                swap(nums[i], nums[j]);
                ++i;
                --j;
            } else return j;
        }
    }
};
