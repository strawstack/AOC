let fs = require('fs');

function sol(data) {

    data = data.map(x => x.split("\n"))

    let allGroups = [];

    for (let packet of data) {
        let group = {};
        for (let line of packet) {
            for (let c of line) {
                group[c] = true;
            }
        }
        allGroups.push(group);
    }

    //console.log(allGroups);

    let count = 0;
    for (let group of allGroups) {
        count += Object.keys(group).length;
    }

    return count;
}

//
// main
//

async function main() {
    let data;
    try {
        data = await readFile('./input.txt');
    } catch(err) { throw err; }

    data = data.substr(0, data.length - 1).split("\n\n");
    let ans = sol(data);

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
