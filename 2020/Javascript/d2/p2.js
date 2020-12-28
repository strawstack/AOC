let fs = require('fs');

async function main() {
    let data = await readFile('./input.txt');
    data = data.split("\n").map(x => x.split(" "));
    data.pop();
    data = data.map(x => [x[0].split("-").map(x => parseInt(x, 10)), x[1][0], x[2]]);

    let count = 0;
    for (let row of data) {
        let word = row[2];
        let c = row[1];
        let a = row[0][0];
        let b = row[0][1];
        let n = 0;
        if (word[a - 1] == c) {
            n += 1;
        }
        if (word[b - 1] == c) {
            n += 1;
        }
        if (n == 1) {
            count += 1;
        }
    }

    return count;
}

function fz(word) {
    let d = {};
    for (let c of word) {
        if (!(c in d)) d[c] = 0;
        d[c] += 1;
    }
    return d;
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
