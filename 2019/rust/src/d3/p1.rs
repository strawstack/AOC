use std::fs;

pub fn main() {
    let fname = "src/d3/input.txt";
    let data: Vec<Vec<(char, i32)>> = fs::read_to_string(fname)
        .expect("read failed")
        .trim().lines() // &str to &[str]
        .map(|line| { // line: &str
            line.trim().split(",") // &[str]
            .map(|t| {
                t.chars().collect::<Vec<char>>() // &[str] to Vec<char>
            })
            .map(|t| { // t: &[char]
                (
                    t[0], // char
                    t[1..].iter()
                        .collect::<String>() // &[char] to String
                        .parse().unwrap() // String to i32
                )
            }).collect() // Vec<(char, i32)>
        }).collect();

    println!("{:?}", data);
}
