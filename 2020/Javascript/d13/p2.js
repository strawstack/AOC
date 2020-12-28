let fs = require('fs');

/*
{ id: 29, delay: 0 },
{ id: 41, delay: 19 },
{ id: 661, delay: 29 },
{ id: 13, delay: 42 },
{ id: 17, delay: 43 },
{ id: 23, delay: 52 },
{ id: 521, delay: 60 },
{ id: 37, delay: 66 },
{ id: 19, delay: 79 }
*/

function sol(data) {

    let arrival = parseInt(data[0]);
    let busList = data[1].split(",").map(x => {
        if (x == "x") {
            return -1;
        } else {
            return parseInt(x);
        }
    });

    let bl = [];
    busList.forEach((n, i) => {
        if (n != -1) {
            bl.push({
                id: n,
                offset: i
            });
        }
    });

    // Init
    let prevSol = 0;
    let _lcm = bl[0].id;

    // Loop pulling one bus ID into the solution each time
    for (let i = 0; i < bl.length - 1; i++) {

        // The next bus to add to the solution
        let nextNum = bl[i + 1];

        // Find a multiple of the previous solution
        // that meets the next criteria in the bus list
        // Eq: ((prevSol + m * _lcm) + offset) % nextNum == 0
        prevSol = find(prevSol, _lcm, nextNum.offset, nextNum.id);

        // Calculate the LCM for all the bus ids seen so far
        _lcm = lcm(_lcm, nextNum.id);
    }

    return prevSol;
}

function find(prevSol, _lcm, offset, b) {
    let mx_lcm = _lcm;
    while (true) {
        if ((((prevSol + mx_lcm) + offset) % b) == 0) {
            return prevSol + mx_lcm;
        }
        mx_lcm += _lcm;
    }
}

function gcd(a,b){
  var t = 0;
  a < b && (t = b, b = a, a = t); // swap them if a < b
  t = a%b;
  return t ? gcd(b,t) : b;
}

function lcm(a, b){
  return a / gcd(a,b) * b;
}

//
// main
//

async function main() {
    let data;
    try {
        data = await readFile('./input.txt');
    } catch(err) { throw err; }

    data = data.trim().split("\n");
    let ans = sol(data);

    if(ans !== undefined) {
        console.log(ans);
    }
}

main().catch(err => console.log(err));

//
// Helper Functions
//

// read file
function readFile(path) {
    return new Promise((res, rej) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) rej(err);
            res(data);
        });
    });
}
