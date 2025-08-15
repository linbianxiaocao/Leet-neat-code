impl Solution {
    pub fn remove_kdigits(num: String, k: i32) -> String {
        let mut stack = Vec::new();
        let mut to_remove = k;

        for (i, c) in num.chars().enumerate() {
            while to_remove > 0 && stack.last().map_or(false, |&last| last > c) {
                stack.pop();
                to_remove -= 1;
            }

            stack.push(c);
        }

        // If we still have digits to remove, remove from the end
        for _ in 0..to_remove {
            stack.pop();
        }

        // Convert stack back to string and remove leading zeros
        let result = stack.into_iter().collect::<String>().trim_start_matches('0').to_string();
        if result.is_empty() { "0".to_string() } else { result }
    }
}
