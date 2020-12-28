let fs = require('fs');

function sol(data) {
    let lst = [];
    for (let row of data) {
        row = row.split(" (contains ");
        let ingre = row[0].split(" ");
        let aller = row[1].slice(0, row[1].length - 1).split(", ");
        lst.push([ingre, aller]);
    }

    // keys are aller
    // values are list of sets
    // sets are all ingre present in foods with given aller
    let setLookup = {};

    for (let item of lst) {
        let ingre = item[0];
        let set_ingre = new Set(ingre);
        let aller = item[1];
        for (_a of aller) {
            if (!(_a in setLookup)) setLookup[_a] = [];
            setLookup[_a].push(set_ingre);
        }
    }

    // Assign to each ingre
    // the union of each list of sets
    let unionLookup = {};
    for (let _a in setLookup) {
        let setList = setLookup[_a];
        let allIntersection = setList[0];
        for (let _set of setList) {
            allIntersection = intersection(allIntersection, _set);
        }
        unionLookup[_a] = allIntersection;
    }

    /*
    for (let k in unionLookup) {
        console.log(k);
        console.log(unionLookup[k]);
        console.log("");
    } */

    // EXAMINE FROM ABOVE OUTPUT TO CALCULATE MAP BELOW 
    let ingreMap = {};
    ingreMap["kdqls"] = "soy";
    ingreMap["mdtvbb"] = "fish";
    ingreMap["kktsjbh"] = "wheat";
    ingreMap["frpvd"] = "peanuts";
    ingreMap["zfcqk"] = "dairy";
    ingreMap["ggdbl"] = "nuts";
    ingreMap["mgczn"] = "sesame";
    ingreMap["zsfzq"] = "shellfish";

    let count = 0;
    for (let item of lst) {
        let ingre = item[0];
        for (let _i of ingre) {
            if (!(_i in ingreMap)) {
                count += 1;
            }
        }
    }

    return count;
}

function union(setA, setB) {
    let _union = new Set(setA)
    for (let elem of setB) {
        _union.add(elem)
    }
    return _union
}

function intersection(setA, setB) {
    let _intersection = new Set()
    for (let elem of setB) {
        if (setA.has(elem)) {
            _intersection.add(elem)
        }
    }
    return _intersection
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
