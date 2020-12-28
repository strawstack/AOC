let fs = require('fs');

function sol(data) {

    data = data.map(x => x.split("\n"))

    let allGroups = [];
    let people = [];

    for (let packet of data) {

        let group = {};
        people.push(packet.length);

        for (let line of packet) {
            for (let c of line) {
                if (!(c in group)) group[c] = 0;
                group[c] += 1;
            }
        }
        allGroups.push(group);
    }

    let count = 0;
    let i = 0;
    for (let group of allGroups) {
        for (let k in group) {
            let value = group[k];
            if (value == people[i]) {
                count += 1;
            }
        }
        i += 1;
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
