// https://www.cnblogs.com/grandyang/p/9615871.html
class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if (!root) return NULL;
        Node *head = NULL, *pre = NULL;
        inorder(root, pre, head);
        pre->right = head;
        head->left = pre;
        return head;
    }
    void inorder(Node* node, Node*& pre, Node*& head) {
        if (!node) return;
        inorder(node->left, pre, head);
        if (!head) {
            head = node;
            pre = node;
        } else {
            pre->right = node;
            node->left = pre;
            pre = node;
        }
        inorder(node->right, pre, head);
    }
};
