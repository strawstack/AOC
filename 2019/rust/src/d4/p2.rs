use std::fs;

pub fn main() {
    let fname = "src/d4/input.txt";
    let data: Vec<i32> = fs::read_to_string(fname)
        .expect("read failed")
        .trim()
        .split("-")
        .map(|x| x.parse().unwrap())
        .collect();

    let lo = (data[0] + 1) as usize;
    let hi = data[1] as usize;

    let mut count = 0;
    for n in lo..hi {
        if check(&n) {
            count += 1;
        }
    }

    println!("{}", count);
}

fn check(n: &usize) -> bool {
    let mut n: i32 = *n as i32;
    let mut inc = true; // Number is non-decreasing
    let mut dbl = false; // Number has double digits somewhere
    let mut dbl2 = false;
    let mut count = 1;
    let mut prev = n % 10;

    //println!("{}", n);

    while n > 0 {
        n = n / 10;
        let cur = n % 10;

        // Check for dbl
        if !dbl2 {
            if prev == cur {
                count += 1;
                if count == 2 {
                    dbl = true;
                } else {
                    dbl = false;
                }
            } else { // prev != cur
                count = 1;
                if dbl {
                    dbl2 = true;
                }
            }
        }

        // Check for non dec
        if cur > prev {
            inc = false;
        }

        prev = cur;
    }

    //println!(" {} {}", inc, dbl);

    return inc && (dbl || dbl2);
}
