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

    //code[520] = {name: 'nop', arg: code[520].arg};

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

    let changeList = [];
    for (let i = 0; i < code.length; i++) {
        if (code[i].name == "jmp" || code[i].name == "nop") {
            changeList.push(i);
        }
    }

    // For each jmp or nop instc
    for (let index of changeList) {

        // Copy code
        let c_code = [];
        for (let item of code) {
            c_code.push({
                "name": item.name,
                "arg": item.arg
            });
        }

        // Flip instc
        if (c_code[index].name == "jmp") {
            c_code[index].name = "nop";
        } else {
            c_code[index].name = "jmp";
        }

        let count = 1500; // break if inf loop
        let flag = false; // signal correct program found
        ac = 0; // reset memory
        pc = 0;
        while (true) {

            if (pc == c_code.length) {
                flag = true;
                break;
            }

            let instc = c_code[pc];

            op[instc.name](instc.arg);

            count -= 1;
            if (count == 0) {
                break;
            }
        }

        if (flag) {
            return ac;
        }
    }
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
