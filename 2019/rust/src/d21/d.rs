mod p1;
mod p2;

pub fn main(part: i32) {
    if part == 2 {
        p2::main();
    } else {
        p1::main();
    }
}
