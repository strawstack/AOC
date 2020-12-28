use std::fs;

pub fn main() {
    let data = fs::read_to_string("src/d1/input.txt").expect("read failed");

    let lst = data.trim().split("\n");

    let mut ns = Vec::new();

    for s in lst {
        ns.push(s.parse::<i32>().unwrap());
    }

    let mut total: i32 = 0;

    for n in ns {
        total += n / 3 - 2;
    }

    println!("{}", total);

    println!(
        "{}",
        fs::read_to_string("src/d1/input.txt")
            .expect("read failed")
            .lines()
            .fold(0, |acc, x| acc + (x.parse::<i32>().unwrap() / 3 - 2))
    );
}
