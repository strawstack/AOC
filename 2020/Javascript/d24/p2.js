let fs = require('fs');

function sol(data) {

    // e, se, sw, w, nw, and ne
    // nw   ne
    //  w t e
    // sw   se

    // track black tiles
    let black = {};

    for (let line of data) {
        let index = 0;
        let loc = {r: 0, c: 0};
        while (index < line.length) {

            // Get the next direction
            let next = undefined;
            if (index == line.length - 1) {
                next = line[index];
            } else {
                next = line.substr(index, 2);
            }

            if (next == "ne") {
                loc.c += (loc.r % 2 == 0) ? 0 : 1;
                loc.r -= 1;
                index += 2;

            } else if (next[0] == "e") {
                loc.c += 1;
                index += 1;

            } else if (next == "se") {
                loc.c += (loc.r % 2 == 0) ? 0 : 1;
                loc.r += 1;
                index += 2;

            } else if (next == "sw") {
                loc.c += (loc.r % 2 == 0) ? -1 : 0;
                loc.r += 1;
                index += 2;

            } else if (next[0] == "w") {
                loc.c -= 1;
                index += 1;

            } else if (next == "nw") {
                loc.c += (loc.r % 2 == 0) ? -1 : 0;
                loc.r -= 1;
                index += 2;

            }
        }
        let h = hash(loc);
        if (!(h in black)) {
            black[h] = true;
        } else {
            black[h] = !black[h];
        }
    }

    let first_count = 0;
    for (let k in black) {
        let v = black[k];
        if (v) {
            first_count += 1;
        }
    }

    //console.log(`ans: ${first_count}`);

    let ROW_MAX = 0;
    let ROW_MIN = 0;
    let COL_MAX = 0;
    let COL_MIN = 0;

    // Simulate flipping
    let times = 100;
    while (times > 0) {

        // Determine max and min
        for (let k in black) {
            let loc = unhash(k);
            ROW_MAX = Math.max(ROW_MAX, loc.r);
            ROW_MIN = Math.min(ROW_MIN, loc.r);
            COL_MAX = Math.max(COL_MAX, loc.c);
            COL_MIN = Math.min(COL_MIN, loc.c);
        }

        ROW_MAX += 1;
        ROW_MIN -= 1;
        COL_MAX += 1;
        COL_MIN -= 1;

        //console.log(ROW_MAX, ROW_MIN, COL_MAX, COL_MIN);

        // Visit each tile and check neighbours
        let nt = {};
        for (let row = ROW_MIN; row <= ROW_MAX; row++) {
            for (let col = COL_MIN; col <= COL_MAX; col++) {
                let cLoc = {r: row, c: col};
                //console.log(cLoc);
                let isBlack = isTileBlack(black, cLoc);
                let nCount = getNeigh(black, cLoc);
                if (isBlack) {
                    if (nCount == 0 || nCount > 2) {
                        nt[hash(cLoc)] = false;
                    } else {
                        nt[hash(cLoc)] = true;
                    }
                } else {
                    if (nCount == 2) {
                        nt[hash(cLoc)] = true;
                    } else {
                        nt[hash(cLoc)] = false;
                    }
                }
            }
        }

        // Copy results
        black = nt;

        let count = 0;
        for (let k in black) {
            let v = black[k];
            if (v) {
                count += 1;
            }
        }

        //console.log(`times: ${100 - times + 1}, count: ${count}`);

        times -= 1;
    }

    let count = 0;
    for (let k in black) {
        let v = black[k];
        if (v) {
            count += 1;
        }
    }

    // wrong - 17
    // wrong - 25
    // wrong - 2208
    return count;
}

function hash(loc) {
    return `${loc.r}:${loc.c}`;
}

function unhash(str) {
    let val = str.split(":");
    let row = parseInt(val[0]);
    let col = parseInt(val[1]);
    return {
        r: row,
        c: col
    };
}

function isTileBlack(black, cLoc) {
    let h = hash(cLoc);
    if (h in black) {
        return black[h];
    } else {
        return false;
    }
}

function getNeigh(black, cLoc) {
    //console.log("call getNeigh");
    let adj = [
        {r: -1, c: (cLoc.r % 2 == 0) ? 0 : 1}, // ne
        {r: 0, c: 1}, // e
        {r: 1, c: (cLoc.r % 2 == 0) ? 0 : 1}, // se
        {r: 1, c: (cLoc.r % 2 == 0) ? -1 : 0}, // sw
        {r: 0, c: -1}, // w
        {r: -1, c: (cLoc.r % 2 == 0) ? -1 : 0} // nw
    ];
    let count = 0;
    for (let a of adj) {
        let nl = {
            r: cLoc.r + a.r,
            c: cLoc.c + a.c
        };
        if (isTileBlack(black, nl)) {
            count += 1;
        }
    }
    return count;
}

//
// main
//

async function main() {
    let data;
    try {
        data = await readFile('./input.txt');
        //data = await readFile('./test_input.txt');
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
