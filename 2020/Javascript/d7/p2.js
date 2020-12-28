let fs = require('fs');

function sol(data) {

    let lookup = {};

    for (let line of data) {
        line = line.replace(/bags/g, "bag"); // standardize bags and bag
        line = line.slice(0, line.length - 5); // trailing " bag."
        let s1 = line.split(" bag contain ");
        let bag_name = s1[0];
        let lst = s1[1].split(" bag, ");
        let f = x => {
            let res = x.match(/(\d+) (.+)/);
            if (res != undefined) {
                return { qty: parseInt(res[1]), name: res[2] };
            }
        };
        lst = lst.map(f);

        if (lst[0] != undefined) {
            lookup[bag_name] = lst;
        } else {
            lookup[bag_name] = [];
        }
    }

    // For each bag type, do a recursize search for gold bags
    let count = 0;
    const gold = "shiny gold";
    for (let bag of lookup[gold]) {
        count += search(lookup, bag);
    }

    return count;
}

function search(lookup, outer) {
    let total = outer.qty;
    for (let bag of lookup[outer.name]) {
        total += outer.qty * search(lookup, bag);
    }
    return total;
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
