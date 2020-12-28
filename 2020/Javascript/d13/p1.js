let fs = require('fs');

function sol(data) {

    let arrival = parseInt(data[0]);
    let busList = data[1].split(",").map(x => {
        if (x == "x") {
            return -1;
        } else {
            return parseInt(x);
        }
    });

    let validBus = busList.filter(x => x > 0);

    let bestId = validBus[0];
    let bestValue = Math.ceil(arrival / bestId) * bestId - arrival;

    for (let id of validBus) {
        let value = Math.ceil(arrival / id) * id - arrival;
        if (value < bestValue) {
            bestId = id;
            bestValue = value;
        }
    }

    return bestId * bestValue;
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
