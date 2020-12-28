let fs = require('fs');

function sol(data) {

    let pc = 0;
    let ac = 0;

    let code = data.map(x => {
        let s = x.split(" ");
        return {
            "name": s[0],
            "arg": parseInt(s[1], 10)
        }
    });

    let op = {
        "acc": (val) => {
            ac += val;
            pc += 1;
        },
        "jmp": (val) => {
            pc += val;
        },
        "nop": (val) => {
            // no op
            pc += 1;
        }
    };

    // what ops have been run
    let run = {};

    while (true) {
        let instc = code[pc];

        if (pc in run) {
            return ac;
        }
        run[pc] = true;

        op[instc.name](instc.arg);
    }

    //return undefined;
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
