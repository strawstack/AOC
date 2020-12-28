let fs = require('fs');

class Node {
    constructor(value, next) {
        this.val = value;
        this.next = next;
    }
}

function sol(data) {
    data = data.split("").map(x => parseInt(x));

    let first = new Node(data[0], undefined);
    data.shift();

    // Create chain from input
    let prev = first;
    for (let n of data) {
        let nextNode = new Node(n, undefined);
        prev.next = nextNode;
        prev = nextNode;
    }

    // Add remaining values to chain
    const ONE_MILLION = 1000000;
    for (let i = 10; i <= ONE_MILLION; i++) {
        let nextNode = new Node(i, undefined);
        prev.next = nextNode;
        prev = nextNode;
    }

    // Quick find values with lookup
    let lookup = {};
    let nx = first;
    let last = undefined;
    while (nx != undefined) {
        lookup[nx.val] = nx;
        if (nx.val == ONE_MILLION) last = nx;
        nx = nx.next;
    }

    // Connect last to first
    // to create a loop
    last.next = first;

    // Run simulation
    let curCup = first; // ref to current cup
    let moves = 10 * ONE_MILLION;
    while (moves > 0) {

        // Identify cups to pick up
        let p1 = curCup.next;
        let p2 = p1.next;
        let p3 = p2.next;

        // Remove picked up cups
        curCup.next = p3.next;

        // Select destination cup
        let d = curCup.val - 1;
        if (d == 0) d = ONE_MILLION;
        while (d == p1.val || d == p2.val || d == p3.val) {
            d -= 1;
            if (d == 0) d = ONE_MILLION;
        }

        // Place cups
        let destCup = lookup[d];
        let temp = destCup.next;
        destCup.next = p1;
        p3.next = temp;

        curCup = curCup.next;
        moves -= 1;
    }

    let oneCup = lookup[1];
    let c1 = oneCup.next;
    let c2 = c1.next;

    return c1.val * c2.val;
}

function pad(val, size) {
    val = val.toString();
    let len = val.length;
    let p = [];
    if (len < size) {
        for (let i = 0; i < size - len; i++) {
            p.push(" ");
        }
    }
    return `${p.join("")}${val}`;
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
