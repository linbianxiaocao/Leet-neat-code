// https://leetcode.com/problems/longest-well-performing-interval/discuss/334565/javacpython-on-solution-life-needs-996-and-669

use std::collections::HashMap;

impl Solution {
    pub fn longest_wpi(hours: Vec<i32>) -> i32 {        
        let mut seen = HashMap::new();
        let mut score = 0;
        let mut res = 0;

        for i in 0..hours.len() {
            if hours[i] > 8 {
                score += 1;
            } else {
                score -= 1;
            }

            if score > 0 { res = i + 1; }
            seen.entry(score).or_insert(i);

            if seen.contains_key(&(score-1)) {
                res = res.max(i - seen[&(score-1)]);
            }
        }

        res as i32
    }
}
