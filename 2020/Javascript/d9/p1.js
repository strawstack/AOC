let fs = require('fs');

function sol(data) {
    data = data.map(x => parseInt(x));

    let curList = [];

    // Pre
    let index = 0;
    while (true) {
        curList.push(data[index]);
        index += 1;
        if (index >= 25) {
            break;
        }
    }

    while (index < data.length) {
        let possible = getPossible(curList);

        if (!(data[index] in possible)) {
            break;
        }

        // Next number
        curList.shift();
        curList.push(data[index]);
        index += 1;
    }

    return data[index];
}

function getPossible(curList) {
    let f = {};
    curList.forEach((a, i) => {
        curList.forEach((b, j) => {
            if (i != j) {
                f[a + b] = true;
            }
        });
    });
    return f;
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
