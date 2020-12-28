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

    let wp = {
        r: -1,
        c: 10
    };

    for (let item of data) {
        let op = item.op;
        let val = item.val;

        if (op == "R") {
            // (c, r) with  (−r, c)
            let turns = Math.floor(val / 90);

            while (turns > 0) {
                wp = {
                    r: wp.c,
                    c: -1 * wp.r
                };
                turns -= 1;
            }

        } else if (op == "L") {
            // (c, r) with (r, −c)
            let turns = Math.floor(val / 90);

            while (turns > 0) {
                wp = {
                    r: -1 * wp.c,
                    c: wp.r
                };
                turns -= 1;
            }

        } else if (op == "F") {
            let _val = val;
            while (_val > 0) {
                loc = {
                    r: loc.r + wp.r,
                    c: loc.c + wp.c
                };
                _val -= 1;
            }

        } else { // N, E, S, W
            let vect = dir[card[op]];
            wp = {
                r: wp.r + val * vect.r,
                c: wp.c + val * vect.c
            };
        }
    }

    let res = Math.abs(loc.r) + Math.abs(loc.c);

    // wrong: 37165
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
