let fs = require('fs');

function sol(data) {

    // Parse input into: rules, mine, others
    let rules = data[0];
    let mine = data[1].split("\n")[1];
    let _others = data[2].split("\n");
    _others.shift();
    let others = _others;

    // Parse rules
    rules = rules.split("\n").map(row => {
        let res = row.match(/^(.+): (\d+)-(\d+) or (\d+)-(\d+)/);
        return {
            name: res[1],
            a: res[2], b: res[3],
            c: res[4], d: res[5]
        };
    });

    // Parse my ticket
    mine = mine.split(",").map(x => parseInt(x));

    // Parse others
    others = others.map(row => row.split(",").map(x => parseInt(x)));

    // Remove invalid tickets
    others = others.filter(ticket => {
        for (let n of ticket) {
            if (failAll(n, rules)) {
                return false;
            }
        }
        return true;
    });

    let banned = [
        {},{},{},{},{},
        {},{},{},{},{},
        {},{},{},{},{},
        {},{},{},{},{}
    ];

    // Find a ticket with a value
    // that only meets one criteria
    others.forEach((ticket, i) => {
        let tlst = [];
        ticket.forEach((n, j) => {
            let vf = validFields(n, rules);
            // console.log(`ticket: ${i}, number: ${j}, vf: ${vf[0]}`);
            if (Object.keys(vf).length == 19) {
                let name = notPresent(rules, vf);
                banned[j][name] = true;
            }
        });
    });

    let field_names = [
        false, false, false, false, false,
        false, false, false, false, false,
        false, false, false, false, false,
        false, false, false, false, false
    ];

    let possible = [];
    banned.forEach((lst, i) => {
        let np = notPresentList(rules, lst);
        possible.push(np);
    });

    while (missing(field_names)) {
        let index = 0;
        let rem = undefined;
        for (let lst of possible) {
            if (lst.length == 1) {
                field_names[index] = lst[0];
                rem = lst[0];
            }
            index += 1;
        }
        for (let i = 0; i < possible.length; i++) {
            let row = possible[i].slice();
            let rm_index = row.indexOf(rem);
            if (rm_index != -1) {
                row.splice(rm_index, 1);
            }
            possible[i] = row;
        }
    }

    let total = 1;
    const TOKEN = "departure";
    field_names.forEach((name, i) => {
        if (name.indexOf(TOKEN) != -1) {
            total *= mine[i];
        }
    });

    return total;
}

// A field name is still null
function missing(field_names) {
    for (let name of field_names) {
        if (name === false) {
            return true;
        }
    }
    return false;
}

function notPresentList(rules, vf) {
    let lst = [];
    for (let rule of rules) {
        let name = rule.name;
        if (!(name in vf)) {
            lst.push(name);
        }
    }
    return lst;
}

// Which rule name is not present in vf
function notPresent(rules, vf) {
    for (let rule of rules) {
        let name = rule.name;
        if (!(name in vf)) {
            return name;
        }
    }
}

function validFields(n, rules) {
    let vf = [];
    for (let rule of rules) {
        if ((n >= rule.a && n <= rule.b) || (n >= rule.c && n <= rule.d)) {
            vf[rule.name] = true;
        }
    }
    return vf;
}

// Number fails all rules
function failAll(n, rules) {
    let count = 0;
    for (let rule of rules) {
        if ((n >= rule.a && n <= rule.b) || (n >= rule.c && n <= rule.d)) {
            count += 1;
        }
    }
    return count == 0;
}

//
// main
//

async function main() {
    let data;
    try {
        data = await readFile('./input.txt');
    } catch(err) { throw err; }

    data = data.trim().split("\n\n");
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
