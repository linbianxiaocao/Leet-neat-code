impl Solution {
    pub fn longest_substring(s: String, k: i32) -> i32 {
        // https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/949666/Rust-sliding-window-solution
        // https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solutions/87739/Java-Strict-O(N)-Two-Pointer-Solution/
        let s = s.as_bytes();
        let mut max = 0;

        for h in 1..=26 {
            // for a fixed h (number of unique characters)
            let mut counts = [0; 26];
            let mut unique = 0;
            let (mut i, mut j) = (0, 0);
            let mut not_less_than_k = 0;
            
            while j < s.len() {
                if unique <= h {
                    let idx = (s[j] - b'a') as usize;
                    if counts[idx] == 0 { unique += 1; }
                    counts[idx] += 1;
                    if counts[idx] == k { not_less_than_k += 1; }
                    j += 1;
                } else {
                    let idx = (s[i] - b'a') as usize;
                    if counts[idx] == k { not_less_than_k -= 1; }
                    counts[idx] -= 1;
                    if counts[idx] == 0 { unique -= 1; }				
                    i += 1;
                }
                
                if unique == h && not_less_than_k == h {
                    max = max.max(j - i);
                }
            }            
        }

        max as i32
    }        
}
