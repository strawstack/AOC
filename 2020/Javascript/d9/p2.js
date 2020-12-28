let fs = require('fs');

function sol(data) {
    data = data.map(x => parseInt(x));
    const TARGET = 542529149;

    let f = () => {
        for (let n = 2; n < data.length; n++) {
            let total = data.slice(0, n);
            for (let i = n; i < data.length; i++) {
                if (sum(total) == TARGET) {
                    //console.log(total);
                    return total;
                }
                total.shift();
                total.push(data[i]);
            }
        }
    };

    let ans = f();
    return Math.min(...ans) + Math.max(...ans);
}

function sum(lst) {
    return lst.reduce((a, b) => a + b, 0);
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
