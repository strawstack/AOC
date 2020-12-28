let fs = require('fs');

function sol(data) {
    data = data.split("").map(x => parseInt(x));
    const MOVES = 100;
    const SIZE = data.length;
    const MIN = Math.min(...data);
    const MAX = Math.max(...data);

    let cv = data[0];
    for (let i = 0; i < MOVES; i++) {
        //console.log(`\n-- move: ${i + 1} --`);
        /* console.log(`cups: ${data.map((v, i) => {
            if (v == cv) {
                return `(${v})`;
            } else {
                return `${v}`;
            }
        }).join(" ")}`); */

        let ri = [];
        let cur = data.indexOf(cv);
        for (let j = 1; j <= 3; j++) {
            ri.push((cur + j) % SIZE);
        }
        let pull = [];
        ri.forEach(index => {
            pull.push(data[index]);
            data[index] = -1;
        });
        data = data.filter(x => x != -1);

        //console.log(`pick up: ${pull.join(", ")}`);
        //console.log(`data: ${data.join(" ")}`);

        let target = cv - 1;
        while (true) {
            //console.log(target);
            let ti = data.indexOf(target);
            if (ti != -1) {
                //console.log(`destination: ${data[ti]}`);
                // Insert cups right after target cup
                data.splice(ti + 1, 0, ...pull);
                cv = data[(data.indexOf(cv) + 1) % SIZE];
                //console.log(`nx cup: ${cv}`);
                break;
            }

            // Update target
            target -= 1;
            if (target < MIN) {
                target = MAX;
            }
        }
    }

    let ans = [];

    // Collect answer clockwise after cup 1
    let oi = data.indexOf(1);
    for (let i = oi + 1; i < oi + data.length; i++) {
        let index = i % data.length;
        ans.push(data[index].toString());
    }

    // wrong - 79463528
    // wrong - 67852394
    return ans.join("");
}

//
// main
//

async function main() {
    let data;
    try {
        data = await readFile('./input.txt');
        //data = await readFile('./test_input.txt');
    } catch(err) { throw err; }

    data = data.trim();
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
