let fs = require('fs');

function sol(data) {
    data = data.map(x => parseInt(x));
    data.sort((a, b) => a - b);

    data.unshift(0);
    data.push(Math.max(...data) + 3);

    let total = {1: 0, 2: 0, 3: 0};
    for (let i = 1; i < data.length; i++) {
        let d = data[i] - data[i - 1];
        total[d] += 1;
    }

    return total[1] * total[3];
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
