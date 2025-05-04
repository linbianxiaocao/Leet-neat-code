
pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
    let mut v: Vec<(i32, f64)> = position.iter().zip(speed.iter())
        .map(|(&pos, &speed)| (pos, (target - pos) as f64 / speed as f64))
        .collect();

    v.sort_by(|a, b| b.0.cmp(&a.0));

    let mut fleets = 0;
    let mut last_time = 0.0;

    for (_, time) in v {
        if time > last_time {
            fleets += 1;
            last_time = time;
        }
    }

    fleets
}


fn main() {
    println!("Hello, world!");
}