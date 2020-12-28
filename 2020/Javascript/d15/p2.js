let fs = require('fs');

/*
Given the starting numbers 1,3,2, the 2020th number spoken is 1.
Given the starting numbers 2,1,3, the 2020th number spoken is 10.
Given the starting numbers 1,2,3, the 2020th number spoken is 27.
Given the starting numbers 2,3,1, the 2020th number spoken is 78.
Given the starting numbers 3,2,1, the 2020th number spoken is 438.
Given the starting numbers 3,1,2, the 2020th number spoken is 1836.
*/

function sol(data) {
    data = data[0].split(",").map(x => parseInt(x));

    let lookup = {};
    for (let i = 0; i < data.length - 1; i++) {
        lookup[data[i]] = i + 1;
    }

    let spoken = data[data.length - 1];
    let turn = data.length + 1;
    while (true) {
        let lastSpoken = spoken;

        if (lastSpoken in lookup) {
            spoken = (turn - 1) - lookup[lastSpoken];

        } else {
            spoken = 0;

        }

        lookup[lastSpoken] = turn - 1;

        if (turn % 1000000 == 0) {
            console.log(`turn: ${turn / 1000000} mil`);
        }

        if (turn == 30000000) {
            return spoken;
        }

        turn += 1;
    }
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
