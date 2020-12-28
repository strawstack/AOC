let fs = require('fs');

function sol(data) {

    let plane = [];
    for (let r = 0; r < 128; r++) {
        plane.push(
            [0, 0, 0, 0, 0, 0, 0, 0]
        );
    }

    let seat_ids = {};
    let seat_ids_list = [];

    for (let row of data) {

        let rb = {lo: 0, hi: 127};
        let cb = {lo: 0, hi: 7};

        for (let letter of row) {
            let mr = Math.floor((rb.lo + rb.hi)/2);
            let mc = Math.floor((cb.lo + cb.hi)/2);

            if (letter == "F") {
                rb = {
                    lo: rb.lo,
                    hi: mr
                };

            } else if (letter == "B") {
                rb = {
                    lo: mr + 1,
                    hi: rb.hi
                };

            } else if (letter == "L") {
                cb = {
                    lo: cb.lo,
                    hi: mc
                };

            } else if (letter == "R") {
                cb = {
                    lo: mc + 1,
                    hi: cb.hi
                };
            }
        }

        seat_ids[rb.lo * 8 + cb.lo] = true;
        seat_ids_list.push(rb.lo * 8 + cb.lo);
    }

    let max = Math.max(...seat_ids_list);
    let min = Math.min(...seat_ids_list);

    let missing = [];

    for (let i = min; i < max + 1; i++) {
        if (!(i in seat_ids)) {
            missing.push(i);
        }
    }

    return missing;
}

//
// main
//

async function main() {
    let data;
    try {
        data = await readFile('./input.txt');
    } catch(err) { throw err; }

    data = data.substr(0, data.length - 1).split("\n");
    let ans = sol(data);

    if(ans !== undefined) {
        console.log(ans);
    }
}

main();

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
