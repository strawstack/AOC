let fs = require('fs');

async function main() {
    let data = await readFile('./input.txt');
    data = data.substr(0, data.length - 1).split("\n");

    let count = 0;

    data = data.map(row => {
        let res = row.match(/^(\d+)-(\d+) (.): (.+)$/);
        let r = {min: p(res[1]), max: p(res[2]), let: res[3], word: res[4]};
        let f = fz(r.word);
        if (r.let in f) {
            let n = f[r.let];
            if (n >= r.min && n <= r.max) {
                count += 1;
            }
        }
    });

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

function p(str) {
    return parseInt(str, 10);
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
