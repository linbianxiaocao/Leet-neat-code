use std::collections::BTreeSet;

struct ExamRoom {
    n: i32,
    seats: BTreeSet<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ExamRoom {

    fn new(n: i32) -> Self {
        ExamRoom { n, seats: BTreeSet::new(), }
    }
    
    fn seat(&mut self) -> i32 {
        if self.seats.is_empty() { self.seats.insert(0); return 0; }

        let mut prev = -1;
        let mut max_dist = 0;
        let mut candidate = 0;

        for &s in &self.seats {
            if prev == -1 {
                if s > max_dist {
                    max_dist = s;
                    candidate = 0;
                }
            } else {
                let dist = (s - prev) / 2;
                if dist > max_dist {
                    max_dist = dist;
                    candidate = prev + dist;
                }
            }
            prev = s;
        }

        if self.n - 1 - self.seats.iter().last().unwrap() > max_dist {
            candidate = self.n - 1;
        }

        self.seats.insert(candidate);
        candidate

    }
    
    fn leave(&mut self, p: i32) {
        self.seats.remove(&p);
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * let obj = ExamRoom::new(n);
 * let ret_1: i32 = obj.seat();
 * obj.leave(p);
 */


fn main() {
    println!("Hello, world!");
}