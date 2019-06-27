/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    // https://www.cnblogs.com/grandyang/p/4295618.html
    // 递归区间是左闭右开[head, tail)
    // 我们也可以采用如下的递归方法，重写一个递归函数，有两个输入参数，子链表的起点和终点，因为知道了这两个点，链表的范围就可以确定了，而直接将中间部分转换为二叉搜索树即可，递归函数中的内容跟上面解法中的极其相似，参见代码如下
    TreeNode* sortedListToBST(ListNode* head) {
        if (!head) return NULL;
        return helper(head, NULL);
    }
    
    TreeNode* helper(ListNode* head, ListNode* tail) {
        if (head == tail) return NULL;
        ListNode *slow = head, *fast = head;
        while (fast != tail && fast->next != tail) {
            slow = slow->next;
            fast = fast->next->next;
        }
        TreeNode *cur = new TreeNode(slow->val);
        cur->left = helper(head, slow);
        cur->right = helper(slow->next, tail);
        
        return cur;
    }
};
