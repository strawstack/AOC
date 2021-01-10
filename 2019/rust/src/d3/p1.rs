use std::fs;
use std::collections::HashSet;
use std::ops::Add;

#[derive(Debug, Hash, Copy, Clone)]
struct Position {
    x: i32,
    y: i32
}

impl Add for Position {
    type Output = Position;

    fn add(self, rhs: Position) -> Position {
        Position{
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        }
    }
}

impl PartialEq for Position {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

impl Eq for Position {}

pub fn main() {
    let fname = "src/d3/input.txt";
    //let fname = "src/d3/test_one.txt"; // 159
    let data: Vec<Vec<(char, i32)>> = fs::read_to_string(fname)
        .expect("read failed")
        .trim().lines() // &str to &[str]
        .map(|line| { // line: &str
            line.trim().split(",") // &[str]
            .map(|t| { // t: &str
                t.chars()
                .collect::<Vec<char>>() // &str to iter[Vec<char>]
            })
            .map(|t| { // t: Vec<char>
                (
                    t[0], // char
                    t[1..].iter()
                        .collect::<String>() // iter[char] to String
                        .parse().unwrap() // String to i32
                )
            }).collect() // Vec<(char, i32)>
        }).collect();

    // Track wires
    let mut hs: HashSet<Position> = HashSet::new();

    // Track intersections
    let mut inter: Vec<Position> = Vec::new();

    let get_delta = |d| {
        match d {
            'U' => Position{x: 1, y: 0},
            'R' => Position{x: 0, y: 1},
            'D' => Position{x: -1, y: 0},
            'L' => Position{x: 0, y: -1},
            _ => Position{x: 0, y: 0},
        }
    };

    let mut pos = Position{x: 0, y: 0};
    for (dir, qty) in &data[0] {
        let d = get_delta(*dir);
        for _ in 0..*qty {
            pos = pos + d;
            hs.insert(pos);
        }
    }

    let mut pos = Position{x: 0, y: 0};
    for (dir, qty) in &data[1] {
        let d = get_delta(*dir);
        for _ in 0..*qty {
            pos = pos + d;
            match hs.get(&pos) {
                Some(p) => inter.push(*p),
                None => ()
            }
        }
    }

    let ans = inter.iter().map(|p| p.x.abs() + p.y.abs()).min();
    println!("{:?}", ans.unwrap());
}
