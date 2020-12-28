let fs = require('fs');

async function main() {
    let data = await readFile('./input.txt');
    let d = {};
    data = data.trim().split("\n").map(x => parseInt(x));
    data.forEach(x => d[x] = true);

    let f = () => {
        for (let n of data) {
            if ((2020 - n) in d) {
                return n * (2020 - n);
            }
        }
    };

    return f();
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
}).catch(err => {
    console.log(err);
});
