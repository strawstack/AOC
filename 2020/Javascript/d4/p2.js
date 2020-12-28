let fs = require('fs');

async function sol() {
    let data = await readFile('./input.txt');
    data = data.substr(0, data.length - 1).split("\n\n");
    /*
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) */
    let req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
    let opt = "cid";

    let reqCheck = {
        "byr": (value) => {
            let len = value.length == 4;
            let val = parseInt(value, 10);
            if (len && val >= 1920 && val <= 2002) {
                return true;
            } else {
                return false;
            }
        },
        "iyr": (value) => {
            let len = value.length == 4;
            let val = parseInt(value, 10);
            if (len && val >= 2010 && val <= 2020) {
                return true;
            } else {
                return false;
            }
        },
        "eyr": (value) => {
            let len = value.length == 4;
            let val = parseInt(value, 10);
            if (len && val >= 2020 && val <= 2030) {
                return true;
            } else {
                return false;
            }
        },
        "hgt": (value) => {
            let res = value.match(/(\d+)(..)/);
            if (res == undefined) return false;
            let num = parseInt(res[1], 10);
            let mes = res[2];
            if (mes == "cm") {
                if (num >= 150 && num <= 193) {
                    return true;
                }
            } else if (mes == "in") {
                if (num >= 59 && num <= 76) {
                    return true;
                }
            }
            return false;
        },
        "hcl": (value) => {
            return /#[0-9a-f]{6}/.test(value);
        },
        "ecl": (value) => {
            let d = {
                "amb": true,
                "blu": true,
                "brn": true,
                "gry": true,
                "grn": true,
                "hzl": true,
                "oth": true
            };
            return value in d;
        },
        "pid": (value) => {
            return /^[0-9]{9}$/.test(value);
        }
    };

    let count = 0;
    for (let item of data) {
        items = item.split(/[\n| ]/);
        pairs = items.map(x => x.split(":"));

        if (allValid(req, reqCheck, pairs)) {
            count += 1;
        }
    }

    return count;
}

let collect = {};

function allValid(req, reqCheck, pairs) {
    let group = {};
    for (let prop of pairs) {
        let p = prop[0];
        group[p] = prop[1];
    }
    for (let r of req) {
        if (!(r in group)) {
            return false;
        }
        let _key = r;
        let _result = reqCheck[r](group[r]);
        if (!(_key in collect)) {
            collect[_key] = [];
        }
        collect[_key].push([group[r], _result]);
        //console.log(r, group[r], reqCheck[r](group[r]));
        if (!(reqCheck[r](group[r]))) {
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
