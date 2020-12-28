let fs = require('fs');

async function main(item) {
    let data = await readFile('./input.txt');
    data = data.split("\n");
    data.pop();
    const COLS = data[0].length;
    const ROWS = data.length;

    let loc = {r: 0, c: 0};
    let move = item;
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

/*
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
*/

async function sol() {
    let ansList = [];

    let lst = [{r: 1, c: 1}, {r: 1, c: 3}, {r: 1, c: 5}, {r: 1, c: 7}, {r: 2, c: 1}];

    for (let item of lst) {
        let ans = await main(item);
        ansList.push(ans);
    }

    let total = 1;
    for (let n of ansList) {
        total *= n;
    }
    return total;
}

sol().then(ans => {
    console.log(ans);
})
