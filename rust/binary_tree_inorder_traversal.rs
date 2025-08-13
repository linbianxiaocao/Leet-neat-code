// https://www.cnblogs.com/zuoyuan/p/3720273.html
// iterative method
impl Solution {
    pub fn inorder_traversal(mut root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res: Vec<i32> = vec![];
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = vec![];

        while root.is_some() || !stack.is_empty() {
            if let Some(node) = root {
                stack.push(Rc::clone(&node));
                root = node.borrow().left.clone();
            }
            else if let Some(node) = stack.pop() {
                res.push(node.borrow().val);
                root = node.borrow().right.clone();
            }
        }

        res
    }
}
