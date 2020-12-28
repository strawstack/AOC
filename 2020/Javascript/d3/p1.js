let fs = require('fs');

async function main() {
    let data = await readFile('./input.txt');
    data = data.split("\n");
    data.pop();
    const COLS = data[0].length;
    const ROWS = data.length;

    let loc = {r: 0, c: 0};
    let move = {r: 1, c: 3};
    let treeCount = 0;

    let hasTree = (loc) => _hasTree(data, ROWS, COLS, loc);

    while (loc.r < ROWS) {
        if (hasTree(loc)) {
            treeCount += 1;
        }
        loc.r += move.r;
        loc.c += move.c;
    }

    return treeCount;
}

function _hasTree(data, ROWS, COLS, loc) {
    let rr = loc.r;
    let cc = loc.c % COLS;
    let value = data[rr][cc];
    return value === "#";
}

function readFile(path) {
    return new Promise((res, rej) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) rej(err);
            res(data);
        });
    });
}

main().then(ans => {
    console.log(ans);
});
