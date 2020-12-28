let fs = require('fs');

async function sol() {
    let data = await readFile('./input.txt');
    data = data.substr(0, data.length - 1).split("\n\n");

    let req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
    // let opt = "cid";

    let count = 0;
    for (let item of data) {
        items = item.split(/[\n| ]/);
        pairs = items.map(x => x.split(":"));

        if (allValid(req, pairs)) {
            count += 1;
        }
    }

    return count;
}

function allValid(req, pairs) {
    let count = 0;
    let group = {};
    for (let prop of pairs) {
        let p = prop[0];
        group[p] = true;
    }
    for (let r of req) {
        if (!(r in group)) {
            return false;
        }
    }
    return true;
}

//
// main
//

async function main() {
    let ans = await sol();
    if(ans !== undefined) {
        console.log(ans);
    }
}

main();

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

// string to frequency dict
function fz(word) {
    let d = {};
    for (let c of word) {
        if (!(c in d)) d[c] = 0;
        d[c] += 1;
    }
    return d;
}

// parseInt
function p(str) {
    return parseInt(str, 10);
}
