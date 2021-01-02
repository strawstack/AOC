use std::fs;

pub fn main() {
    let data = fs::read_to_string("src/d1/input.txt").expect("read failed");

    let lines: Vec<i64> = data.lines().map(|x| x.parse::<i64>().unwrap()).collect();

    let mut total: i64 = 0;

    for x in lines {
        total += calc(x);
    }

    println!("{}", total);
}

fn calc(n: i64) -> i64 {
    let mut total: i64 = 0;
    let mut x = n;

    loop {
        x = x / 3 - 2;
        if x <= 0 {
            break;
        }
        total += x;
    }

    return total;
}
