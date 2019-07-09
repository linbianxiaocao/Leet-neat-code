class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/5136749.html
    // https://leetcode.com/problems/create-maximum-number/discuss/77286/Short-Python-Ruby-C%2B%2B
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<int> res;
        int n1 = nums1.size(), n2 = nums2.size();
        for (int i = max(0, k-n2); i <= min(k, n1); ++i)
            res = max(res, mergeVector(maxVector(nums1, i), maxVector(nums2, k-i)));
        return res;
        
    }
    
    // create max number of length t from single non-empty vector
    // suppose num = [4, 9, 3, 2, 1, 8, 7, 6], we need to create maximum vetor with length t from 1 to 8
    // t = 8, res = [4, 9, 3, 2, 1, 8, 7, 6]
    // t = 7, drop 4, res = [9, 3, 2, 1, 8, 7, 6]
    // t = 6, drop 1, res = [9, 3, 2, 8, 7, 6]
    // t = 5, drop 2, res = [9, 3, 8, 7, 6]
    // t = 4, drop 3, res = [9, 8, 7, 6]
    // for t = 3, 2, 1, drop a number from the end each time
    // see a nice explanation in https://leetcode.com/problems/create-maximum-number/discuss/77287/C%2B%2B-16ms-FASTEST-beats-97.
    vector<int> maxVector(vector<int>& nums, int t) {
        int drop = nums.size() - t;
        vector<int> res;
        for (int num : nums) {
            while (drop > 0 && !res.empty() && res.back() < num) {
                res.pop_back();
                --drop;
            }                            
            res.push_back(num);
        }
        res.resize(t);
        return res;
    }
    

    // this is the regular merge, which doesn't work with this example
    // nums1 = [6, 7]
    // nums2 = [6, 0, 4]
    // k = 5
    // ans = [6, 7, 6, 0, 4]
    // It seems obvious, we should always choose the larger one right? This is correct, but the problem is what should we do if they are equal? This is not so obvious. The correct answer is we need to see what behind the two to decide. 
    // https://web.archive.org/web/20160120093629/http://algobox.org/create-maximum-number/
    // vector<int> mergeVector(vector<int> nums1, vector<int> nums2) {
    //     vector<int> res;
    //     int i = 0, j = 0;
    //     while (i < nums1.size() && j < nums2.size()) {
    //         if (nums1[i] > nums2[j]) res.push_back(nums1[i++]);
    //         else res.push_back(nums2[j++]);
    //     }
    //     while (i < nums1.size()) res.push_back(nums1[i++]);
    //     while (j < nums2.size()) res.push_back(nums2[j++]);
    //     return res;
    // }
    
    vector<int> mergeVector(vector<int> nums1, vector<int> nums2) {
        vector<int> res;
        while (!nums1.empty() || !nums2.empty()) {
            vector<int>& tmp = (nums1 > nums2) ? nums1 : nums2;
            res.push_back(tmp[0]);
            tmp.erase(tmp.begin());
        }
        return res;
    }
    
};