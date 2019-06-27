// https://www.cnblogs.com/grandyang/p/4298069.html

// 这道题的真正符合要求的解法应该用的Morris遍历，这是一种非递归且不使用栈，空间复杂度为O(1)的遍历方法，可参见我之前的博客 Binary Tree Inorder Traversal，在其基础上做些修改，加入first, second和parent指针，来比较当前节点值和中序遍历的前一节点值的大小，跟上面递归算法的思路相似，代码如下：
