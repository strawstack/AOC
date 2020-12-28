let fs = require('fs');

function sol(data) {

    let d0 = data[0].split("\n");
    let d1 = data[1].split("\n");
    d0.shift();
    d1.shift();
    let p = d0.map(x => parseInt(x));
    let c = d1.map(x => parseInt(x));

    while (p.length > 0 && c.length > 0) {

        let pd = p.shift();
        let cd = c.shift();

        if (pd > cd) {

            p.push(pd);
            p.push(cd);

        } else {

            c.push(cd);
            c.push(pd);

        }
    }

    let winner = (p.length == 0) ? c : p;

    let total = 0;
    let length = winner.length;
    for (let card of winner) {
        total += card * length;
        length -= 1;
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
        //data = await readFile('./test_input.txt');
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
