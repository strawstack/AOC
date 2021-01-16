use std::fs;
use std::io::{self, BufRead};

pub fn main() {
    let mut mem: Vec<i32> = fs::read_to_string("src/d2/input.txt")
        .expect("read failed")
        .trim().split(",")
        .map(|x| x.parse().unwrap())
        .collect();

    // Init
    // mem[1] = 12;

    // Program counter
    let mut pc: i32 = 0;

    loop {

        let op: i32 = mem[pc as usize];

        // Get value from mem
        let get_mem = |x: i32| mem[x as usize];

        match op {
            1 => {
                let a = mem[get_mem(pc + 1) as usize];
                let b = mem[get_mem(pc + 2) as usize];
                let c = get_mem(pc + 3);
                //println!("a: {}, b: {}, c: {}", a, b, c);
                mem[c as usize] = a + b;
                pc += 4;
            },
            2 => {
                let a = mem[get_mem(pc + 1) as usize];
                let b = mem[get_mem(pc + 2) as usize];
                let c = get_mem(pc + 3);
                //println!("a: {}, b: {}, c: {}", a, b, c);
                mem[c as usize] = a * b;
                pc += 4;
            },
            3 => {
                let a = mem[get_mem(pc + 1) as usize];
                let mut line = String::new();
                let stdin = io::stdin();
                stdin.lock().read_line(&mut line).unwrap();
                let data = line.parse::<i32>().unwrap();
                mem[a as usize] = data;
            },
            4 => {
                let a = mem[get_mem(pc + 1) as usize];
                print!("{}", a);
            },
            99 => {
                break;
            },
            a => panic!("Unknown opcode: {}", a),
        }
    }

    println!("{:?}", mem[0]);
}
