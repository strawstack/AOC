let fs = require('fs');

function sol(data) {

    const card = parseInt(data[0]);
    const door = parseInt(data[1]);
    const m = 20201227;
    const subject_number = 7;

    let value = 1;
    let card_loop = 0;
    while (value != card) {
        value *= subject_number;
        value = value % m;
        card_loop += 1;
    }

    value = 1;
    let door_loop = 0;
    while (value != door) {
        value *= subject_number;
        value = value % m;
        door_loop += 1;
    }

    console.log(`card loop: ${card_loop}`);
    console.log(`door loop: ${door_loop}`);

    let loop = door_loop;
    value = 1;
    while (loop) {
        value *= card;
        value = value % m;
        loop -= 1;
    }

    let ans = value;

    console.log(`key: ${ans}`);

    // wrong: 5236149
    // wrong: 5995558
    return ans;
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
