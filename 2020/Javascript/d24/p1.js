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

    let count = 0;
    for (let k in black) {
        let v = black[k];
        if (v) {
            count += 1;
        }
    }

    return count;
}

function hash(loc) {
    return `${loc.r}:${loc.c}`;
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
