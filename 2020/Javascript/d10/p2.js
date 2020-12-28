let fs = require('fs');

function sol(data) {
    data = data.map(x => parseInt(x));
    data.sort((a, b) => a - b);

    data.unshift(0);
    data.push(Math.max(...data) + 3);

    // From left to right, add one at a time

    // Example
    // base
    // 0 - A - B - C
    // B asks if A is needed
    // C asks if B is needed and if A - B is needed
    // D asks about C and B - C

    // For each index, from 0
    // How many combinations are possible?

    let ans = [1, 1];
    if ((data[2] - data[0]) <= 3) {
        ans.push(2);
    } else {
        ans.push(1);
    }

    for (let i = 3; i < data.length; i++) {
        let base = data[i - 3];
        let a = data[i - 2];
        let b = data[i - 1];
        let c = data[i];

        // Possibilities for previous chains
        let baseCount = ans[ans.length - 3];
        let aCount = ans[ans.length - 2];
        let bCount = ans[ans.length - 1];

        let cCount = bCount;

        // Can we remove AB?
        if ((c - base) <= 3) {
            cCount += baseCount;
        }

        // Can we remove B?
        if ((c - a) <= 3) {
            cCount += aCount;
        }

        ans.push(cCount);
    }

    // wrong - 7923826688
    // wrong - 839808
    // wrong - 75144747810816
    // wrong - 1073741824
    // correct - 6044831973376
    return ans[ans.length - 1];
}

function hash(lst) {
    return lst.map(x => x.toString()).join(":");
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
