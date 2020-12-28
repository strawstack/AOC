use std::env;

#[path = "d1/d.rs"]
mod d1;
#[path = "d2/d.rs"]
mod d2;
#[path = "d3/d.rs"]
mod d3;
#[path = "d4/d.rs"]
mod d4;
#[path = "d5/d.rs"]
mod d5;
#[path = "d6/d.rs"]
mod d6;
#[path = "d7/d.rs"]
mod d7;
#[path = "d8/d.rs"]
mod d8;
#[path = "d9/d.rs"]
mod d9;
#[path = "d10/d.rs"]
mod d10;

#[path = "d11/d.rs"]
mod d11;
#[path = "d12/d.rs"]
mod d12;
#[path = "d13/d.rs"]
mod d13;
#[path = "d14/d.rs"]
mod d14;
#[path = "d15/d.rs"]
mod d15;
#[path = "d16/d.rs"]
mod d16;
#[path = "d17/d.rs"]
mod d17;
#[path = "d18/d.rs"]
mod d18;
#[path = "d19/d.rs"]
mod d19;
#[path = "d20/d.rs"]
mod d20;

#[path = "d21/d.rs"]
mod d21;
#[path = "d22/d.rs"]
mod d22;
#[path = "d23/d.rs"]
mod d23;
#[path = "d24/d.rs"]
mod d24;
#[path = "d25/d.rs"]
mod d25;

fn main() {
    let args: Vec<String> = env::args().collect();

    let mut day = 1;
    let mut part = 1;

    if args.len() < 3 || args.len() > 3 {
        println!("cargo run [day] [part]");

    } else {
        day = args[1].parse::<i32>().unwrap();
        part = args[2].parse::<i32>().unwrap();

    }

    let days: Vec<fn(i32) -> ()> = vec![
        |p| d1::main(p),
        |p| d2::main(p),
        |p| d3::main(p),
        |p| d4::main(p),
        |p| d5::main(p),
        |p| d6::main(p),
        |p| d7::main(p),
        |p| d8::main(p),
        |p| d9::main(p),
        |p| d10::main(p),

        |p| d11::main(p),
        |p| d12::main(p),
        |p| d13::main(p),
        |p| d14::main(p),
        |p| d15::main(p),
        |p| d16::main(p),
        |p| d17::main(p),
        |p| d18::main(p),
        |p| d19::main(p),
        |p| d20::main(p),

        |p| d21::main(p),
        |p| d22::main(p),
        |p| d23::main(p),
        |p| d24::main(p),
        |p| d25::main(p),
    ];

    days[(day - 1) as usize](part as i32);
}
