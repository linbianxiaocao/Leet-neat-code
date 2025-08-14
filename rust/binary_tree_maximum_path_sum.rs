// (a)
pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max_sum = i32::MIN;
        Self::rec(root, &mut max_sum);
        max_sum
    }

    fn rec(node: Option<Rc<RefCell<TreeNode>>>, max_sum: &mut i32) -> i32 {
        if let Some(n) = node {
            let left_max = Self::rec(n.borrow().left.clone(), max_sum);
            let right_max = Self::rec(n.borrow().right.clone(), max_sum);

            let mut curr_max = n.borrow().val;
            if left_max > 0 {
                curr_max += left_max;
            }
            if right_max > 0 {
                curr_max += right_max;
            }

            *max_sum = (*max_sum).max(curr_max);

            left_max.max(right_max).max(0) + n.borrow().val
        } else {
            0
        }
    }

// (b)
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max_sum = i32::MIN;
        Self::rec(&root, &mut max_sum);
        max_sum
    }

    fn rec(node: &Option<Rc<RefCell<TreeNode>>>, max_sum: &mut i32) -> i32 {
        if let Some(n) = node {
            let left_max = Self::rec(&n.borrow().left, max_sum);
            let right_max = Self::rec(&n.borrow().right, max_sum);

            let mut curr_max = n.borrow().val;
            if left_max > 0 { curr_max += left_max; }
            if right_max > 0 { curr_max += right_max; }
        
            *max_sum = (*max_sum).max(curr_max);
            n.borrow().val + left_max.max(right_max).max(0)
        } else {
            0
        }
    }
