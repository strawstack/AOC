let fs = require('fs');

function sol(data) {

    // Parse input into: rules, mine, others
    let rules = data[0];
    let mine = data[1].split("\n")[1];
    let _others = data[2].split("\n");
    _others.shift();
    let others = _others;

    // Parse rules
    rules = rules.split("\n").map(row => {
        let res = row.match(/^(.+): (\d+)-(\d+) or (\d+)-(\d+)/);
        return {
            name: res[1],
            a: res[2], b: res[3],
            c: res[4], d: res[5]
        };
    });

    // Parse others
    others = others.map(row => row.split(",").map(x => parseInt(x)));


    // Count invalid
    let total = 0;
    for (let row of others) {
        for (let n of row) {
            if (failAll(n, rules)) {
                total += n;
            }
        }
    }

    // wrong - 2389608
    return total;
}

// Number fails all rules
function failAll(n, rules) {
    let count = 0;
    for (let rule of rules) {
        if ((n >= rule.a && n <= rule.b) || (n >= rule.c && n <= rule.d)) {
            count += 1;
        }
    }
    return count == 0;
}

//
// main
//

async function main() {
    let data;
    try {
        data = await readFile('./input.txt');
    } catch(err) { throw err; }

    data = data.trim().split("\n\n");
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
