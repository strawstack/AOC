use std::fs;

pub fn main() {
    let fname = "src/d5/input.txt";
    //let fname = "src/d5/input_test.txt";
    let mut mem: Vec<i32> = fs::read_to_string(fname)
        .expect("read failed")
        .trim().split(",")
        .map(|x| x.parse().unwrap())
        .collect();

    // Program counter
    let mut pc: i32 = 0;

    // debug
    let d = false;

    loop {

        let (m3, m2, m1, op) = get_flags(mem[pc as usize]);

        if d {
            println!("\n***");
            println!("pc: {}", pc);
            println!("num: {}", mem[pc as usize]);
            println!("m1: {}, m2: {}, m3: {}, op: {}", m1, m2, m3, op);
            println!("***\n");
        }

        // Get value from mem
        let get_mem = |x: i32, f: bool| {
            let val = mem[x as usize];
            if f {
                if d { println!("  {}", val); }
                val
            } else {
                if d { println!("  {} ({})", mem[val as usize], val); }
                mem[val as usize]
            }
        };

        match op {
            1 => {
                if d { println!(" add"); }
                let a = get_mem(pc + 1, m1);
                let b = get_mem(pc + 2, m2);
                let c = get_mem(pc + 3, true);
                pc += 4;
                mem[c as usize] = a + b;
            },
            2 => {
                if d { println!(" mul"); }
                let a = get_mem(pc + 1, m1);
                let b = get_mem(pc + 2, m2);
                let c = get_mem(pc + 3, true);
                pc += 4;
                mem[c as usize] = a * b;
            },
            3 => {
                if d { println!(" input"); }
                let a = get_mem(pc + 1, true);
                pc += 2;

                //print!("input: ");
                //io::stdout().flush().unwrap();

                //let mut line = String::new();
                //let stdin = io::stdin();
                //stdin.lock().read_line(&mut line).unwrap();
                //let data = line.trim().parse::<i32>().unwrap();
                let data = 1;
                mem[a as usize] = data;
            },
            4 => {
                if d { println!(" output"); }
                let a = get_mem(pc + 1, m1);
                pc += 2;

                println!("OUTPUT: {}", a);
            },
            99 => {
                break;
            },
            a => panic!("Unknown opcode: {}", a),
        }
    }

    //println!("{:?}", mem[0]);
}

fn get_flags(num: i32) -> (bool, bool, bool, i32) {
    let op = num % 100;
    let m1 = (num / 100) % 10;
    let m2 = (num / 1000) % 10;
    let m3 = (num / 10000) % 10;
    let tb = |n| n != 0; // number to bool
    return (tb(m3), tb(m2), tb(m1), op);
}
