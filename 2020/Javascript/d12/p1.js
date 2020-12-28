let fs = require('fs');

function sol(data) {

    data = data.map(x => {
        return {
            op: x[0],
            val: parseInt(x.substr(1, x.length - 1))
        }
    });

    // Number to direction vector
    let dir = [
        {r: -1, c: 0},
        {r: 0, c: 1},
        {r: 1, c: 0},
        {r: 0, c: -1}
    ];

    // Cardinal direction to number
    let card = { "N": 0, "E": 1, "S": 2, "W": 3 };

    // 0 - North, 1 - East, 2 - South, 3 - West
    let facing = 1;

    // Current location
    let loc = {
        r: 0,
        c: 0
    };

    for (let item of data) {
        let op = item.op;
        let val = item.val;

        if (op == "L") {
            let turns = Math.floor(val / 90);
            facing = (facing - turns) % 4;
            if (facing < 0) facing += 4;

        } else if (op == "R") {
            let turns = Math.floor(val / 90);
            facing = (facing + turns) % 4;
            if (facing < 0) facing += 4;

        } else if (op == "F") {
            let vect = dir[facing];
            loc = {
                r: loc.r + val * vect.r,
                c: loc.c + val * vect.c
            };

        } else { // N, E, S, W
            let vect = dir[card[op]];
            loc = {
                r: loc.r + val * vect.r,
                c: loc.c + val * vect.c
            };
        }
    }

    let res = Math.abs(loc.r) + Math.abs(loc.c);

    return res;
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
